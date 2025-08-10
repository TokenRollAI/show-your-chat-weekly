# Show Your Chat Weekly

这是 [Show Your Chat](https://github.com/TokenRollAI/show-your-chat) 项目的官方周报网站。

## 项目信息

- **域名**: [show-your-chat.tokenroll.ai](https://show-your-chat.tokenroll.ai)
- **主项目**: [TokenRollAI/show-your-chat](https://github.com/TokenRollAI/show-your-chat)
- **技术栈**: Hexo 静态网站生成器

## 本地开发

### 安装依赖

```bash
npm install
# 或者
pnpm install
```

### 启动开发服务器

```bash
npm run server
# 或者
pnpm run server
```

访问 http://localhost:4000 查看网站

### 构建静态文件

```bash
npm run build
# 或者
pnpm run build
```

### 清理缓存

```bash
npm run clean
# 或者
pnpm run clean
```

## 内容管理

### 创建新的周报

```bash
hexo new post "周报标题"
```

### 创建新页面

```bash
hexo new page "页面名称"
```

## 部署

构建完成后，`public` 目录包含所有静态文件，可以部署到任何静态网站托管服务。

## 贡献

欢迎提交 Pull Request 来改进网站内容和功能！

## 许可证

本项目采用 MIT 许可证。
