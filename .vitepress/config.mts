import { defineConfig } from "vitepress";

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "202.192.143.160",
  vite: {
    css: {
      preprocessorOptions: {
        scss: { api: "modern-compiler" },
      },
    },
  },
  head: [
    [
      "script",
      {
        async: "",
        src: "https://www.googletagmanager.com/gtag/js?id=G-L7L40CR05D",
      },
    ],
    [
      "script",
      {},
      `window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'TAG_ID');`,
    ],
    [
      "script",
      {
        async: "",
        src: "https://busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js",
      },
    ],
    [
      "script",
      {},
      `var _hmt = _hmt || [];
      (function() {
        var hm = document.createElement("script");
        hm.src = "https://hm.baidu.com/hm.js?053c5dfae9ef25676e39e69ec398db69";
        var s = document.getElementsByTagName("script")[0]; 
        s.parentNode.insertBefore(hm, s);
      })();`,
    ],
  ],
  themeConfig: {
    nav: [
      { text: "Home", link: "/" },
      {
        text: "Guide",
        link: "/guide",
      },
    ],
    sidebar: [
      {
        text: "Home",
        link: "/",
      },
      {
        text: "Guide",
        link: "/guide",
      },
      {
        text: "第2章: 传感器与控制",
        collapsed: true,
        items: [
          { text: "第1节: 启动小车", link: "/answers/2/1" },
          { text: "第2节: 控制小车的方向", link: "/answers/2/2" },
          { text: "第3节: 控制小车通过U型赛道", link: "/answers/2/3" },
          { text: "第4节: 控制小车行完成指定道路", link: "/answers/2/4" },
          { text: "第5节: 车载传感器的认识及应用", link: "/answers/2/5" },
          { text: "第6节: 小车巡线行驶", link: "/answers/2/6" },
          { text: "第7节: 小车测距行驶", link: "/answers/2/7" },
          { text: "第8节: 复杂线路下小车的测距行驶", link: "/answers/2/8" },
        ],
      },
      {
        text: "第3章: 机器学习",
        collapsed: true,
        items: [
          { text: "第1节: 通过线性回归预测牧羊犬体重", link: "/answers/3/1" },
          { text: "第2节: 通过多项式回归预测牧羊犬体重", link: "/answers/3/2" },
          { text: "第3节: 线性回归模型评估与测试集", link: "/answers/3/3" },
          { text: "第4节: 线性分类预测性别", link: "/answers/3/4" },
          { text: "第5节: 利用身高和体重预测性别", link: "/answers/3/5" },
          { text: "第6节: 利用感知器完成鸢尾花分类", link: "/answers/3/6" },
          { text: "第7节: 利用支持向量机完成鸢尾花分类", link: "/answers/3/7" },
          { text: "第8节: 分类器的测试与应用", link: "/answers/3/8" },
          { text: "第9节: 理解K均值算法", link: "/answers/3/9" },
        ],
      },
      {
        text: "第4章: 人工神经网络",
        collapsed: true,
        items: [
          { text: "第1节: 利用神经网络完成商区分类任务", link: "/answers/4/1" },
          { text: "第2节: 基于身高预测体重", link: "/answers/4/2" },
        ],
      },
      {
        text: "第5章: 图像处理",
        collapsed: true,
        items: [
          { text: "第1节: 图像的像素和色彩", link: "/answers/5/1" },
          { text: "第2节: 图像的色彩变换", link: "/answers/5/2" },
          { text: "第3节: 图像特效的制作", link: "/answers/5/3" },
          { text: "第4节: 图像扭曲", link: "/answers/5/4" },
          { text: "第5节: 人脸关键点检测", link: "/answers/5/5" },
          { text: "第6节: 动态表情包制作", link: "/answers/5/6" },
        ],
      },
      {
        text: "第6章: 计算机视觉",
        collapsed: true,
        items: [
          { text: "第1节: 利用图像特征完成图像识别", link: "/answers/6/1" },
          { text: "第2节: 利用深度神经网络完成图像分类", link: "/answers/6/2" },
          { text: "第3节: 提取照片中的人脸特征", link: "/answers/6/3" },
          { text: "第4节: 相册中的人脸聚类", link: "/answers/6/4" },
          { text: "第5节: 理解视频中的光流", link: "/answers/6/5" },
          {
            text: "第6节: 利用光流直方图完成行为识别任务",
            link: "/answers/6/6",
          },
          { text: "第7节: 用生成对抗网络生成明星图片", link: "/answers/6/7" },
        ],
      },
      {
        text: "第7章: 文本分析",
        collapsed: true,
        items: [
          { text: "第1节: 字符串和文本文件的读写", link: "/answers/7/1" },
          { text: "第2节: 字典和词频统计", link: "/answers/7/2" },
          { text: "第3节: 课文文章特征提取", link: "/answers/7/3" },
          { text: "第4节: 课文难度分类", link: "/answers/7/4" },
          { text: "第5节: 提取文本特征", link: "/answers/7/5" },
          { text: "第6节: 发掘文本中的潜在主题", link: "/answers/7/6" },
        ],
      },
    ],
    socialLinks: [
      { icon: "github", link: "https://github.com/mcitem/202.192.143.160/" },
    ],
  },
});
