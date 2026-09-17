---
id: 2026-09-17-002
date: 2026-09-17
issue: 9
title: 星星为什么会“眨眼”，行星却通常不会？
slug: why-stars-twinkle-but-planets-usually-do-not
category: 宇宙与地球
category_slug: universe-earth
tags: [星星, 行星, 大气湍流, 闪烁, 自适应光学]
tag_slugs:
  星星: stars
  行星: planets
  大气湍流: atmospheric-turbulence
  闪烁: scintillation
  自适应光学: adaptive-optics
difficulty: 入门
reading_minutes: 7
summary: 星星看起来忽明忽暗、位置轻微跳动，主要不是恒星本身在快速变化，而是星光穿过地球湍动大气时不断被折射。行星具有可分辨的视直径，多条光路的扰动会相互平均，因此通常比恒星稳定。
quick_read:
  - 日常看到的快速“星星闪烁”主要发生在地球大气中，专业术语是天文闪烁或 scintillation。
  - 温度和密度不断变化的湍流空气像一组持续变化的弱透镜，使星光的方向和强度快速波动。
  - 恒星极远，对地面观测者近似点光源；行星则有有限视直径，不同光路受到的扰动会部分平均，所以通常不明显闪烁。
  - 靠近地平线的恒星往往闪得更厉害，因为星光斜穿过更长的大气路径。
  - 现代大型地面望远镜使用自适应光学和激光导星实时测量并补偿这种大气畸变。
evidence_status: verified
images:
  - path: assets/images/2026/09/17/star-trails-eso.jpg
    download_url: https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Star_trails_%28starstax%29.jpg/1280px-Star_trails_%28starstax%29.jpg
    original_url: https://commons.wikimedia.org/wiki/File:Star_trails_(starstax).jpg
    alt: 长曝光夜空照片中恒星形成围绕天极的弧形星轨
    caption: ESO 长曝光星轨照片。恒星的缓慢视运动来自地球自转，而肉眼看到的快速闪烁则主要来自大气湍流。
    credit: A. Duro/ESO
    license: Creative Commons Attribution 4.0 International
  - path: assets/images/2026/09/17/vlt-laser-guide-stars.jpg
    download_url: https://www.eso.org/public/archives/images/screen/2017_11_18_upr_IMG_3305-laser-ok-CC.jpg
    original_url: https://commons.wikimedia.org/wiki/File:Four_lasers_light_up_Paranal_(45564317841).jpg
    alt: 智利帕拉纳尔天文台的甚大望远镜向夜空发射四束橙色激光
    caption: VLT 的激光导星系统在约90千米高空激发钠原子，帮助自适应光学测量并校正大气造成的像差。
    credit: ESO/P. Horálek
    license: Creative Commons Attribution 2.0 Generic
sources:
  - title: Why do stars twinkle?
    organization: NASA Goddard Space Flight Center — Imagine the Universe!
    url: https://imagine.gsfc.nasa.gov/ask_astro/night_sky.html
    tier: 1
    accessed: 2026-09-17
  - title: Adaptive Optics
    organization: European Southern Observatory
    url: https://elt.eso.org/public/teles-instr/technology/adaptive_optics/
    tier: 1
    accessed: 2026-09-17
  - title: Curiosities — Why do stars appear to twinkle in the night sky?
    organization: University of Wisconsin–Madison
    url: https://news.wisc.edu/curiosities-why-do-stars-appear-to-twinkle-in-the-night-sky/
    tier: 2
    accessed: 2026-09-17
  - title: Stellar Scintillation — Why Stars Twinkle
    organization: Sky & Telescope
    url: https://skyandtelescope.org/astronomy-resources/why-do-stars-twinkle/
    tier: 2
    accessed: 2026-09-17
quiz:
  - question: 肉眼看到恒星快速闪烁的主要原因是什么？
    options: [恒星每秒都在剧烈改变能量输出, 地球大气湍流不断改变星光传播路径, 地球自转周期性遮挡恒星]
    answer: 1
    explanation: 不同温度和密度的空气团不断移动，使折射条件快速变化，从而造成位置和亮度波动。
  - question: 为什么行星通常比恒星更少闪烁？
    options: [行星完全不经过大气成像, 行星有有限视直径，多条光路的扰动会相互平均, 行星发出的光比恒星稳定]
    answer: 1
    explanation: 行星在天空中不是理想点源，其盘面不同位置的光穿过不同大气区域，波动会部分平均。
  - question: 为什么低空恒星往往闪烁更明显？
    options: [低空恒星离地球更近, 光线需要斜穿过更长的大气路径, 地平线附近恒星温度更低]
    answer: 1
    explanation: 靠近地平线时，星光经过的大气路径更长，受到更多湍流层影响。
generation:
  source: chatgpt-automation
  automated: true
  pipeline_version: "3.0"
---

## 星星其实没有在那样快速地“眨眼”

晴朗夜晚里，亮星常常一会儿变亮、一会儿变暗，甚至快速闪出红、蓝等颜色。直觉上很容易以为这是恒星自身亮度变化，但我们日常肉眼看到的秒级闪烁，主要发生在光抵达地球后的最后一段路——大气层。

NASA 将这种现象解释为大气中的湍流空气团造成的折射变化。不同空气团的温度、密度和湿度不同，折射率也略有差异。它们不断移动，就像许多形状和焦距都在变化的弱透镜。来自恒星的光穿过这些区域时，传播方向、聚焦程度都会持续改变，于是恒星的视位置和到达眼睛的光强快速波动。这就是天文“闪烁”（scintillation）的一部分。

## 为什么恒星特别容易受影响？

关键不在于恒星小，而在于它们太远。即使恒星真实直径可能达到数十万乃至数百万千米，从地球看，大多数恒星仍近似一个极小的点光源。当大气把这束近似来自单一点的光稍微偏折时，变化不会被同一目标的其他大量独立光路充分抵消，所以眼睛很容易察觉它在抖动和闪烁。

恒星越靠近地平线，闪烁通常越明显。原因不是它突然变得不稳定，而是视线以更倾斜的角度穿过大气，需要经过更长的空气路径，遇到的温度和密度起伏更多。NASA 和多家天文机构都把这一点列为低空亮星——例如天狼星——特别容易强烈闪烁的原因。

[[image:1]]

## 行星为什么看起来稳得多？

肉眼看木星、金星时，它们似乎也只是一个亮点，但从光学角度看，它们与遥远恒星不同。太阳系行星距离近得多，因此在天空中具有有限的视直径，可以视为由许多相邻点共同组成的小圆盘。

这些不同位置发出的或反射的光，会穿过略有不同的大气区域。某一路光暂时被湍流偏向一边时，另一路可能正好向另一方向变化；大量波动叠加后，整体亮度和位置变化被部分平均。因此“行星不闪”更准确的说法应是“行星通常闪烁得不明显”。在大气极不稳定、行星非常靠近地平线等情况下，行星仍可能出现可见闪动。

## 天文学家为什么讨厌浪漫的星光闪烁？

对肉眼而言，闪烁很漂亮；对需要解析细节的地面望远镜而言，它意味着图像被持续扭曲。天文学家把这种由大气造成的成像质量限制称为 seeing。即使望远镜镜面制造得极其精确，大气湍流仍会让本应尖锐的星点膨胀和抖动。

现代大型望远镜因此发展出“自适应光学”。以 ESO 的甚大望远镜为例，激光可在大约90千米高空激发钠原子，制造人工导星。系统快速测量这颗人工星被大气扭曲的方式，再让可变形镜面实时反向调整，抵消一部分湍流造成的像差。换句话说，天文学家先精确测出天空怎样把星光“弄皱”，再让望远镜把它尽可能“熨平”。

这也解释了为什么太空望远镜拥有天然优势：一旦把望远镜送到大气层之外，造成日常恒星闪烁的这层动态光学介质就不再挡在镜头前面。
