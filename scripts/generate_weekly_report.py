#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import os
import sys
from github import Github

def generate_weekly_report():
    # 从环境变量获取GitHub token
    github_token = os.environ.get('GITHUB_TOKEN')
    if not github_token:
        raise ValueError("GITHUB_TOKEN environment variable is required")
    
    gh = Github(github_token)
    repo = gh.get_repo("TokenRollAI/show-your-chat")
    
    # 获取过去7天的issues
    last7days = datetime.datetime.now() - datetime.timedelta(days=7)
    
    try:
        chat_issues = list(repo.get_issues(state="open", since=last7days, labels=["#Chat"]))
        prompt_issues = list(repo.get_issues(state="open", since=last7days, labels=["#Prompt"]))
        greats = list(repo.get_issues(state="open", since=last7days, labels=["!Great!"]))
    except Exception as e:
        print(f"Error fetching issues: {e}")
        # 如果获取失败，创建空列表
        chat_issues = []
        prompt_issues = []
        greats = []
    
    today = datetime.datetime.now().strftime("%Y%m%d")
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 生成markdown内容
    markdown = f"""---
title: Show Your Chat 周报 - {today} 
date: {current_time}
categories:
  - 周报
---

# Show Your Chat 周报 - {today}

## 强烈推荐!

{"".join([f"- [{issue.title}]({issue.html_url})\n" for issue in greats]) if greats else "本周暂无强烈推荐内容。\n"}

## 本周的Chat 

{"".join([f"- [{issue.title}]({issue.html_url})\n" for issue in chat_issues]) if chat_issues else "本周暂无新的Chat分享。\n"}

## 本周的Prompt

{"".join([f"- [{issue.title}]({issue.html_url})\n" for issue in prompt_issues]) if prompt_issues else "本周暂无新的Prompt分享。\n"}

## 关于Show Your Chat

项目的Slogan: [Code is cheap, show me your chat.](https://blog.pdjjq.org/archives/code-is-cheap-show-me-your-chat-kgv2z)

[Github链接](https://github.com/TokenRollAI/show-your-chat)

欢迎star, 欢迎投稿. 欢迎分享你和AI的Chat. 
"""
    
    # 确保目录存在
    weekly_dir = "source/_posts/weekly"
    os.makedirs(weekly_dir, exist_ok=True)
    
    # 写入文件
    file_path = f"{weekly_dir}/{today}.md"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(markdown)
    
    print(f"Weekly report generated: {file_path}")
    print(f"Found {len(greats)} great issues, {len(chat_issues)} chat issues, {len(prompt_issues)} prompt issues")

if __name__ == "__main__":
    generate_weekly_report()
