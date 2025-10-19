# GitHub操作模拟

## 创建远程仓库并关联
```bash
# 在GitHub上创建新仓库 "mydjangoproject"
# 关联本地仓库与远程仓库
git remote add origin https://github.com/username/mydjangoproject.git
```

## 推送到GitHub远程仓库
```bash
# 添加所有文件到暂存区
git add .

# 提交更改
git commit -m "初始提交：创建Django博客项目"

# 推送到远程仓库的主分支
git push -u origin main
```

## Fork Django开源项目
```bash
# 在GitHub上Fork Django项目
# 克隆Fork的仓库到本地
git clone https://github.com/username/django.git

# 添加上游仓库
git remote add upstream https://github.com/django/django.git
```

## 创建功能分支修复bug并提交PR
```bash
# 创建新分支
git checkout -b fix-documentation-typo

# 修改文件
# ...

# 提交更改
git add .
git commit -m "修复文档中的拼写错误"

# 推送到Fork的仓库
git push origin fix-documentation-typo

# 在GitHub上创建Pull Request
```

## 团队协作项目实践
```bash
# 克隆团队项目
git clone https://github.com/team/project.git

# 创建功能分支
git checkout -b feature-user-authentication

# 实现功能并提交
git add .
git commit -m "实现用户认证功能"

# 推送分支
git push origin feature-user-authentication

# 创建Pull Request并请求团队成员审核
```