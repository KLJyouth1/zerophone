# StepGUI Mobile Control - GitHub Actions 自动编译指南

## 简介

本项目已配置GitHub Actions自动化构建，可以自动编译Android APK文件。

## 使用方法

### 步骤1：创建GitHub仓库

1. 访问 GitHub：https://github.com
2. 创建新仓库：`zerophone`
3. 上传项目文件：
   ```bash
   cd c:\Users\Administrator\Desktop\Pad\.trae\documents\zerophone
   git init
   git add .
   git commit -m "Initial commit: StepGUI Mobile Control"
   git branch -M main
   git remote add origin https://github.com/你的用户名/zerophone.git
   git push -u origin main
   ```

### 步骤2：触发自动构建

1. 访问您的GitHub仓库
2. 点击 **"Actions"** 标签
3. 您会看到 "Build Android APK" 工作流
4. 点击 **"Run workflow"** 按钮
5. 选择分支（main），点击 **"Run workflow"**

### 步骤3：下载编译好的APK

构建完成后：

1. 进入 **Actions** > **Build Android APK**
2. 点击最新的 workflow run
3. 在 **Artifacts** 部分下载：
   - **debug-apk**: Debug版本（用于测试）
   - **release-apk**: Release版本（用于发布）

## 构建产物

```
app/build/outputs/apk/debug/
└── app-debug.apk    # Debug版本APK

app/build/outputs/apk/release/
└── app-release.apk  # Release版本APK（需要签名）
```

## 功能说明

### 自动构建

- ✅ 每次push到main分支自动构建
- ✅ 每次Pull Request自动构建
- ✅ 支持手动触发构建

### 代码质量检查

- ✅ Lint代码检查
- ✅ 单元测试（如果配置）

### 构建产物

- 📦 Debug APK - 用于测试和开发
- 📦 Release APK - 用于发布（需要签名）
- 📊 构建报告
- 🧪 测试结果

## 手动构建

如果需要在本地构建，需要安装：

- JDK 17+
- Android SDK (API 34)
- Gradle 8.3+

```bash
# Debug版本
./gradlew assembleDebug

# Release版本
./gradlew assembleRelease
```

## GitHub Actions 配置

工作流文件位置：`.github/workflows/build.yml`

包含三个任务：
1. **build** - 编译APK
2. **lint** - 代码质量检查
3. **test** - 单元测试

## 常见问题

### Q: 构建失败怎么办？
A: 查看Actions日志中的错误信息，常见问题：
- 网络超时（重试）
- 依赖版本不兼容（检查build.gradle.kts）
- 代码语法错误（修复后重新push）

### Q: 如何修改构建配置？
A: 编辑 `.github/workflows/build.yml` 文件

### Q: 如何添加单元测试？
A: 在 `app/src/test/` 目录下添加测试类

### Q: 如何发布Release版本？
A: 
1. 创建tag：`git tag v1.0.0`
2. 推送tag：`git push origin v1.0.0`
3. GitHub Actions会自动构建并创建Release

## 注意事项

1. GitHub Actions每月有2000分钟免费构建时间
2. 构建产物保留7天
3. 首次构建可能需要较长时间（下载依赖）
4. 请确保代码质量，Lint检查失败会阻止合并

## 更多信息

- [GitHub Actions文档](https://docs.github.com/en/actions)
- [Android构建配置](https://developer.android.com/studio/build)
- [Gradle文档](https://docs.gradle.org/)

## 许可证

MIT License
