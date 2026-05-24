# Changelog

本项目所有重要变更记录于此文件。格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)，版本号遵循 [Semantic Versioning](https://semver.org/lang/zh-CN/)。

> 发布日期由 release workflow 在构建时自动注入到 GitHub/Gitea Release 页面，本文件版本标题不再手填日期。

## [Unreleased]

## [v0.2.0]

### Added
- 激光/手电键：按下右键时自动按一下 `laser_key`（开激光），松开右键时再按一下（关激光），以吃上激光带来的开镜速度加成
- `config.ini` 新增 `laser_key`（默认 `y`，留空即关闭此功能）和 `laser_hold`（按一下的持续毫秒数，默认 10）

### Changed
- 打包出的 `df-scope-hold.exe` 加上图标（在文件资源管理器、任务管理器、桌面快捷方式中可识别）

## [v0.1.0]

首个正式发布版本。

### Added
- 监听鼠标右键按下/松开，自动模拟绑定的"屏息"键（默认 `F12`）
- 进程门控：仅在目标游戏进程运行时激活监听，游戏关闭自动停止，重启自动恢复
- `config.ini` 配置文件，可自定义按键、按键延迟（毫秒）、目标进程名
- Windows 单 exe 分发，内嵌 UAC manifest，双击自动请求管理员权限
- GitHub Actions 自动构建 Windows exe，构建完成后同时发布到 GitHub Releases 与 Gitea Releases，方便不同网络环境下载（zip 包含 exe + 默认 config.ini + README）

### Notes
- 游戏客户端通常以管理员权限运行，本工具必须以同等权限运行才能检测到游戏进程
- 仅在 Windows 上验证（三角洲行动客户端为 Windows 独占）
