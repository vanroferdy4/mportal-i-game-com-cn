import json
from datetime import datetime

SITES = [
    {
        "name": "爱游戏平台",
        "url": "https://mportal-i-game.com.cn",
        "tags": ["游戏", "门户", "移动端"],
        "description": "提供在线游戏与互动娱乐服务的综合平台",
        "keywords": ["爱游戏", "游戏平台", "手游"]
    },
    {
        "name": "爱游戏社区",
        "url": "https://mportal-i-game.com.cn/community",
        "tags": ["社区", "讨论", "玩家"],
        "description": "玩家交流、攻略分享与活动资讯社区",
        "keywords": ["爱游戏", "社区", "游戏讨论"]
    },
    {
        "name": "爱游戏商城",
        "url": "https://mportal-i-game.com.cn/shop",
        "tags": ["商城", "道具", "充值"],
        "description": "游戏道具、礼包与会员服务在线商城",
        "keywords": ["爱游戏", "商城", "充值"]
    },
    {
        "name": "爱游戏开发者",
        "url": "https://mportal-i-game.com.cn/dev",
        "tags": ["开发", "API", "SDK"],
        "description": "面向游戏开发者的接入文档与技术支持",
        "keywords": ["爱游戏", "开发者", "API"]
    }
]

def format_tags(tags: list) -> str:
    return ", ".join(tags)

def format_keywords(keywords: list) -> str:
    return " | ".join(keywords)

def generate_summary(site: dict) -> str:
    lines = []
    lines.append(f"站点名称: {site['name']}")
    lines.append(f"  URL: {site['url']}")
    lines.append(f"  标签: {format_tags(site['tags'])}")
    lines.append(f"  关键词: {format_keywords(site['keywords'])}")
    lines.append(f"  说明: {site['description']}")
    return "\n".join(lines)

def build_structured_report(sites: list) -> dict:
    report = {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_sites": len(sites),
        "sites": []
    }
    for site in sites:
        report["sites"].append({
            "name": site["name"],
            "url": site["url"],
            "tags": site["tags"],
            "keywords": site["keywords"],
            "description": site["description"]
        })
    return report

def generate_all_summaries(sites: list) -> list:
    summaries = []
    for site in sites:
        summaries.append(generate_summary(site))
    return summaries

def write_summary_to_file(summaries: list, filepath: str = "summary_output.txt") -> None:
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("站点摘要报告\n")
        f.write("=" * 40 + "\n")
        for idx, summary in enumerate(summaries, 1):
            f.write(f"\n--- 站点 {idx} ---\n")
            f.write(summary + "\n")
    print(f"摘要已写入 {filepath}")

def print_json_report(report: dict) -> None:
    print(json.dumps(report, ensure_ascii=False, indent=2))

def main() -> None:
    print("正在生成爱游戏站点摘要...\n")
    summaries = generate_all_summaries(SITES)
    for idx, summary in enumerate(summaries, 1):
        print(f"=== 站点 {idx} ===")
        print(summary)
        print()

    report = build_structured_report(SITES)
    print("结构化 JSON 报告:")
    print_json_report(report)

    write_summary_to_file(summaries)

if __name__ == "__main__":
    main()