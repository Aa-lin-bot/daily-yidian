---
id: 2026-09-10-001
date: 2026-09-10
issue: 2
title: 天空为什么是蓝色，而夕阳却会变红？
slug: why-is-the-sky-blue
category: 宇宙与地球
category_slug: universe-earth
tags: [天空, 瑞利散射, 大气, 光]
tag_slugs:
  天空: sky
  瑞利散射: rayleigh-scattering
  大气: atmosphere
  光: light
difficulty: 入门
reading_minutes: 7
summary: 蓝天和红色夕阳其实是同一个物理过程的两面：空气分子更擅长散射短波长可见光，而太阳高度决定了光要穿过多长的大气路径。
quick_read:
  - 太阳光看起来是白色的，但包含不同波长的可见光。
  - 对远小于可见光波长的空气分子，短波长光发生瑞利散射更强，强度近似与波长的四次方成反比。
  - 天空没有显得紫色，是因为太阳光谱、上层大气吸收以及人眼对不同波长的敏感度共同影响了最终视觉结果。
  - 日出日落时阳光穿过更长的大气路径，更多蓝紫光被散射出直视方向，因此太阳附近更容易呈现橙红色。
evidence_status: verified
images:
  - path: assets/images/2026/09/10/blue-sky.jpg
    download_url: https://upload.wikimedia.org/wikipedia/commons/f/f0/Blue_sky_image.jpg
    original_url: https://commons.wikimedia.org/wiki/File:Blue_sky_image.jpg
    alt: 蓝色晴空中有少量白云，画面边缘可见棕榈叶
    caption: 晴朗白昼中的蓝色天空
    credit: Renukarenu1861
    license: CC0 1.0 Universal Public Domain Dedication
  - path: assets/images/2026/09/10/rayleigh-scattering.svg
    download_url: https://upload.wikimedia.org/wikipedia/commons/b/be/Rayleigh_sunlight_scattering-int.svg
    original_url: https://commons.wikimedia.org/wiki/File:Rayleigh_sunlight_scattering-int.svg
    alt: 示意不同波长太阳光在地球大气中的瑞利散射强度
    caption: 瑞利散射对短波长可见光更强的示意图
    credit: Д.Ильин；图中理论曲线基于 Robert A. Rohde 的相关图示
    license: CC0 1.0 Universal Public Domain Dedication
  - path: assets/images/2026/09/10/sunset-clouds.jpg
    download_url: https://upload.wikimedia.org/wikipedia/commons/6/6d/Sunset_with_Clouds.jpg
    original_url: https://commons.wikimedia.org/wiki/File:Sunset_with_Clouds.jpg
    alt: 太阳接近地平线，云层被夕阳染成橙红色
    caption: 日落时更长的大气光程使暖色调更加突出
    credit: Xoqoni Said
    license: CC0 1.0 Universal Public Domain Dedication
sources:
  - title: Why Is the Sky Blue?
    organization: NOAA NESDIS
    url: https://www.nesdis.noaa.gov/about/k-12-education/atmosphere/why-the-sky-blue
    tier: 1
    accessed: 2026-09-10
  - title: Why Is the Sky Blue?
    organization: NASA Space Place
    url: https://spaceplace.nasa.gov/blue-sky/en/
    tier: 1
    accessed: 2026-09-10
  - title: Why Is The Sky Blue?
    organization: U.S. National Weather Service
    url: https://www.weather.gov/fgz/SkyBlue
    tier: 1
    accessed: 2026-09-10
  - title: Global Radiation and Aerosols — Red Sky
    organization: NOAA Global Monitoring Laboratory
    url: https://gml.noaa.gov/grad/about/redsky/
    tier: 1
    accessed: 2026-09-10
quiz:
  - question: 为什么晴朗天空主要呈蓝色？
    options: [空气本身含蓝色颜料, 空气分子对短波长可见光散射更强, 海洋把蓝光反射到天空]
    answer: 1
    explanation: 空气分子尺度远小于可见光波长时，瑞利散射对短波长光明显更强。
  - question: 日落时太阳附近为什么更容易呈橙红色？
    options: [太阳温度在傍晚降低, 阳光经过更长的大气路径后更多短波光被散射出直视方向, 地球自转让红光速度变快]
    answer: 1
    explanation: 低太阳高度使直射光经历更长的大气路径，蓝紫等短波成分被更充分地散射。
  - question: 如果一个天体几乎没有大气，在被太阳照亮时远离太阳方向的天空通常会怎样？
    options: [仍然明亮湛蓝, 更接近黑暗, 一定呈红色]
    answer: 1
    explanation: 缺少足够的气体分子，就缺少把太阳光散射到各个视线方向的介质。
generation:
  source: chatgpt-automation
  automated: true
  pipeline_version: "3.0"
---
## 蓝色并不是空气的“本色”

太阳光看上去近似白色，但可见光实际上包含从紫到红的一系列波长。光进入地球大气后，会与氮、氧等气体分子相互作用。对于尺寸远小于可见光波长的散射体，主要机制可以用瑞利散射描述：散射强度近似与波长的四次方成反比。于是波长较短的蓝紫光，比波长较长的红光更容易被空气分子改变传播方向。

这意味着，当你抬头看远离太阳的一块天空时，进入眼睛的很多光并不是从太阳直线射来的，而是太阳光先在大气中被分子散射，再从各个方向进入眼睛。短波长成分更容易走上这条“拐弯路线”，所以天空呈现蓝色。

[[image:1]]

## 那为什么不是紫色？

紫光波长比蓝光更短，单看瑞利散射规律，它甚至应该散射得更强。因此“因为蓝光波长最短，所以天空是蓝色”其实是不准确的简化。

我们真正看到的颜色还取决于进入大气的太阳光谱、不同波长在大气中的吸收，以及人眼视觉系统的响应。NOAA 和美国国家气象局的科普资料都指出，人眼对蓝光比对紫光更敏感，同时部分紫外和紫色成分会受到上层大气影响。多种因素叠加后，我们的视觉系统把晴空感知为蓝色，而不是纯紫色。

<div class="fact"><strong>一个重要修正：</strong>瑞利散射不是“只散射蓝光”。所有可见光都会散射，只是短波长成分明显更强。</div>

## 同一个机制，为什么又制造了红色夕阳？

太阳高悬时，直射阳光穿过的大气路径相对较短；接近日出或日落时，光线以很低的角度穿过大气，到达观察者前要经历更长路径。一路上，蓝紫等短波长成分有更多机会被散射到其他方向，于是沿着太阳方向直接到达眼睛的光中，红、橙、黄等较长波长所占比例上升。

因此蓝天与红色夕阳并不是两个互不相关的现象。白天你看到的是“被散射进视线的短波光”；看夕阳时，你更多看到的是“经历长距离传播后仍留在直射方向的较长波长光”。

[[image:2]]

## 云为什么通常又是白色的？

云滴的尺度通常比单个空气分子大得多，与可见光波长相比已不能简单套用分子尺度的瑞利散射。较大的水滴会更均衡地散射不同可见波长，因此许多薄云或受光充分的云看起来接近白色。厚云之所以会灰暗，则主要是因为光在云体中经历多次散射、吸收和遮蔽后，到达观察者的光减少。

这也说明“物体尺寸”是理解天空颜色的重要条件：空气分子、烟尘、气溶胶和云滴尺寸不同，对光的散射方式也不同。火山灰、污染物或烟雾增多时，天空和夕阳的颜色因此可能发生明显变化。

## 月球上的天空为什么是黑的？

如果几乎没有大气，就没有足够的气体分子把阳光散射到天空的各个方向。月球表面在阳光照射下可以非常明亮，但远离太阳的天空背景仍接近黑色。换句话说，我们习以为常的“明亮天空”，本身就是大气存在的视觉证据之一。

下次看到蓝天或红色夕阳，可以把它理解为一次巨大而持续的光学实验：太阳提供宽谱光源，大气提供散射介质，而你的眼睛就是最后的探测器。
