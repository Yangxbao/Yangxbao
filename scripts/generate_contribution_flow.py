#!/usr/bin/env python3
"""生成「点阵流光」贡献日历动画 SVG（亮 / 暗双主题）。

数据来源：GitHub GraphQL contributionsCollection（使用 Actions 注入的 GITHUB_TOKEN）。
输出：dist/calendar-light.svg、dist/calendar-dark.svg
动画：一道光脉冲沿时间轴从左到右扫过全年格子，有提交的格子亮起并泛起柔光，循环播放。
"""
import json
import os
import urllib.request
from datetime import date

API_URL = "https://api.github.com/graphql"

QUERY = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        weeks {
          contributionDays { date contributionCount }
        }
      }
    }
  }
}
"""

CELL, GAP = 13, 3
PITCH = CELL + GAP
PAD_X, PAD_Y = 26, 26
CAPTION_H = 36
PERIOD = 14.0   # 一次完整扫光周期（秒）
SWEEP = 0.62    # 扫过整年所用周期占比，其余时间静止休眠

FONT = "'Segoe UI',system-ui,-apple-system,'PingFang SC','Microsoft YaHei',sans-serif"

THEMES = {
    "dark": {
        "bg": "#161B22", "stroke": None, "empty": "#20262E",
        "levels": ["#0E4429", "#006D32", "#26A641", "#39D353"],
        "caption": "#8B949E", "glow": "#39D353", "band_peak": 0.22,
    },
    "light": {
        "bg": "#FFFFFF", "stroke": "#D8DEE4", "empty": "#EBEDF0",
        "levels": ["#9BE9A8", "#40C463", "#30A14E", "#216E39"],
        "caption": "#57606A", "glow": "#40C463", "band_peak": 0.16,
    },
}


def fetch_calendar(login: str, token: str):
    body = json.dumps({"query": QUERY, "variables": {"login": login}}).encode()
    req = urllib.request.Request(
        API_URL,
        data=body,
        headers={
            "Authorization": "Bearer " + token,
            "User-Agent": "contribution-flow-action",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        payload = json.load(resp)
    weeks = payload["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    today = date.today().isoformat()
    grid = []
    for week in weeks:
        row = []
        for day in week["contributionDays"]:
            future = day["date"] > today
            row.append({"count": 0 if future else day["contributionCount"]})
        while len(row) < 7:
            row.append({"count": 0})
        grid.append(row)
    return grid


def level_of(count: int) -> int:
    if count <= 0:
        return -1
    if count <= 2:
        return 0
    if count <= 5:
        return 1
    if count <= 9:
        return 2
    return 3


def render(theme_name: str, grid) -> str:
    t = THEMES[theme_name]
    weeks = len(grid)
    grid_w = weeks * PITCH - GAP
    grid_h = 7 * PITCH - GAP
    width = PAD_X * 2 + grid_w
    height = PAD_Y + grid_h + CAPTION_H
    total = sum(cell["count"] for row in grid for cell in row)
    sweep_t = PERIOD * SWEEP
    sweep_x0, sweep_x1 = -60.0, width + 40.0

    base_cells, glow_cells = [], []
    for w, row in enumerate(grid):
        x = PAD_X + w * PITCH
        x_c = PAD_X + w * PITCH + CELL / 2.0
        # 期望光带中心在 t_w 时刻到达本周；SMIL begin 取负相位：闪光发生在 PERIOD-offset 时刻
        t_w = sweep_t * (x_c - sweep_x0) / (sweep_x1 - sweep_x0)
        offset = "{:.3f}".format(PERIOD - t_w)
        for d, cell in enumerate(row):
            y = PAD_Y + d * PITCH
            rect = ('<rect x="{x}" y="{y}" width="{c}" height="{c}" rx="3"').format(
                x=x, y=y, c=CELL
            )
            lvl = level_of(cell["count"])
            if lvl < 0:
                base_cells.append(rect + ' fill="%s"/>' % t["empty"])
                continue
            color = t["levels"][lvl]
            base_cells.append(
                rect
                + ' fill="%s">' % color
                + '<animate attributeName="opacity" values="0.85;1;0.85;0.85" '
                + 'keyTimes="0;0.02;0.16;1" dur="%gs" begin="-%ss" repeatCount="indefinite"/>'
                % (PERIOD, offset)
                + "</rect>"
            )
            glow_cells.append(
                rect
                + ' fill="%s">' % t["glow"]
                + '<animate attributeName="opacity" values="0;0.85;0;0" '
                + 'keyTimes="0;0.02;0.16;1" dur="%gs" begin="-%ss" repeatCount="indefinite"/>'
                % (PERIOD, offset)
                + "</rect>"
            )

    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" '
        'role="img" aria-label="贡献日历点阵流光动画">' % (width, height, width, height),
        '<defs><filter id="glow" x="-60%%" y="-60%%" width="220%%" height="220%%">'
        '<feGaussianBlur stdDeviation="3.2"/></filter>'
        '<linearGradient id="bandGrad" x1="0" y1="0" x2="1" y2="0">'
        '<stop offset="0" stop-color="%s" stop-opacity="0"/>'
        '<stop offset="0.5" stop-color="%s" stop-opacity="%.2f"/>'
        '<stop offset="1" stop-color="%s" stop-opacity="0"/>'
        '</linearGradient></defs>'
        % (t["glow"], t["glow"], t["band_peak"], t["glow"]),
    ]
    bg = '<rect width="%d" height="%d" rx="18" fill="%s"' % (width, height, t["bg"])
    if t["stroke"]:
        bg += ' stroke="%s" stroke-width="1"' % t["stroke"]
    parts.append(bg + "/>")
    parts.extend(base_cells)
    band_values = "%g 0;%g 0;%g 0" % (sweep_x0, sweep_x1, sweep_x1)
    parts.append(
        '<rect x="-15" y="%d" width="30" height="%d" rx="15" fill="url(#bandGrad)">'
        '<animateTransform attributeName="transform" type="translate" values="%s" '
        'keyTimes="0;%.2f;1" dur="%gs" repeatCount="indefinite"/>'
        '<animate attributeName="opacity" values="0;1;1;0;0" '
        'keyTimes="0;0.02;0.58;%.2f;1" dur="%gs" repeatCount="indefinite"/>'
        "</rect>" % (PAD_Y - 8, grid_h + 16, band_values, SWEEP, PERIOD, SWEEP, PERIOD)
    )
    parts.append('<g filter="url(#glow)">')
    parts.extend(glow_cells)
    parts.append("</g>")

    caption_y = PAD_Y + grid_h + 24
    caption = (
        '<text x="%d" y="%d" font-family="%s" font-size="13" fill="%s">'
        "✦ 每一笔提交都在发光</text>" % (PAD_X, caption_y, FONT, t["caption"])
    )
    stat = (
        '<text x="%d" y="%d" text-anchor="end" font-family="%s" font-size="13" fill="%s">'
        "%d contributions · 近一年</text>" % (width - PAD_X, caption_y, FONT, t["caption"], total)
    )
    parts.append(caption)
    parts.append(stat)
    parts.append("</svg>")
    return "".join(parts)


def main():
    repo = os.environ.get("GITHUB_REPOSITORY", "Yangxbao/Yangxbao")
    login = repo.split("/")[0]
    token = os.environ["GITHUB_TOKEN"]
    grid = fetch_calendar(login, token)
    os.makedirs("dist", exist_ok=True)
    for name in ("light", "dark"):
        svg = render(name, grid)
        path = "dist/calendar-%s.svg" % name
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg)
        print(path, "written,", len(svg), "bytes")


if __name__ == "__main__":
    main()
