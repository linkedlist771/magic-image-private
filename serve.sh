#!/bin/bash

echo "🔨 正在构建项目..."
npm run build
npx serve@latest out -l tcp://0.0.0.0:8080