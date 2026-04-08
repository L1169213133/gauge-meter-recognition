# Gauge Meter Recognition

[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/opencv-4.x-green.svg)](https://opencv.org/)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)
[![Computer Vision](https://img.shields.io/badge/category-Computer%20Vision-orange.svg)](https://en.wikipedia.org/wiki/Computer_vision)

## 项目简介

基于计算机视觉的**仪表识别与检测系统**，能够自动识别仪表盘的圆形轮廓、定位指针位置并计算读数。本项目是上海电力大学《计算机视觉》课程实验项目，采用Hough圆变换和边缘分析技术，实现了高精度的仪表读数自动识别。

![Gauge Detection Result](gauge_result/result.jpg)

## 实验目的

1. 掌握计算机视觉中圆形检测、边缘检测等基本技术
2. 学习仪表盘指针定位和读数计算的算法原理
3. 理解Hough变换在圆形检测中的应用
4. 培养图像处理和模式识别的实践能力
5. 实现仪表读数的自动识别与显示

## 技术原理

### 仪表识别基本原理

仪表识别是工业自动化和智能监控系统中的重要技术，主要通过图像处理算法识别仪表盘的指针位置并计算读数。本实验采用基于Hough圆检测和边缘分析的方法：

1. **图像预处理**：将彩色图像转换为灰度图，减少计算复杂度
2. **边缘检测**：使用Canny算法检测图像边缘
3. **圆形检测**：使用Hough圆变换定位仪表盘
4. **指针定位**：通过360度角度搜索找到指针位置
5. **读数计算**：根据指针角度计算仪表读数（0-100标准化）
6. **结果可视化**：在原图上绘制检测结果和读数

### 关键技术

- **Canny边缘检测**：采用双阈值检测，有效提取仪表盘和指针边缘
- **Hough圆变换**：用于检测仪表盘的圆形轮廓
- **角度搜索**：通过360度扫描寻找指针位置（1度步长）
- **轮廓分析**：当Hough变换失败时，使用轮廓分析作为备用方案
- **射线采样**：在射线上采样10个点，提高边缘强度计算的准确性

## 功能特点

- **高精度检测**：Hough圆变换能够准确检测仪表盘位置
- **双重检测机制**：Hough圆检测 + 轮廓分析，提高检测可靠性
- **精确读数**：通过360度角度搜索，实现指针位置的精确检测（1度步长）
- **鲁棒性强**：具备备用方案，当圆检测失败时使用轮廓分析
- **实时性好**：算法复杂度适中，能够满足实时检测需求
- **可视化清晰**：使用不同颜色标注，便于结果分析和理解
- **标准化输出**：将角度转换为0-100的标准化读数（保留一位小数）

## 环境要求
- Python 3.6+
- OpenCV 4.x
- NumPy

## 项目结构

| 文件 | 说明 |
|------|------|
| `20257007-李振-仪表识别实验.docx` | 实验报告文档 |
| `test2.py` | 仪表识别主程序 |
| `yibiao1.jpg` | 测试输入图像 |
| `yibiao1_result.jpg` | 检测结果图像 |

## 实验结果
- 黄色圆圈：检测到的仪表盘轮廓
- 红色指针：检测到的仪表指针位置
- 红色数字：计算出的仪表读数（保留一位小数，范围0-100）

![yibiao1_result](https://github.com/user-attachments/assets/6af2c2dc-6a9b-4372-8482-ddc64e4ebb7c)




