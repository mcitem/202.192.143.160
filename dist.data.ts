import { defineLoader } from "vitepress";
export interface Data {
  cate: string;
  items: {
    name: string;
    chapter: string;
    url: string;
    link: string;
  }[];
}
declare const data: Data[];
export { data };
export default defineLoader({
  load(): Data[] {
    return [
      {
        cate: "全部",
        items: [
          {
            name: "传感器与控制: 启动小车",
            chapter: "第2章 第1节",
            url: "/images/2.1你的专属小车.png",
            link: "/answers/2/1",
          },
          {
            name: "传感器与控制: 控制小车的方向",
            chapter: "第2章 第2节",
            url: "/images/2.2虚拟小车的转弯.png",
            link: "/answers/2/2",
          },
          {
            name: "传感器与控制: 控制小车通过U型赛道",
            chapter: "第2章 第3节",
            url: "/images/2.4通过U形赛道.png",
            link: "/answers/2/3",
          },
          {
            name: "传感器与控制: 控制小车行完成指定道路",
            chapter: "第2章 第4节",
            url: "/images/2.6重复任务与循环结构.png",
            link: "/answers/2/4",
          },
          {
            name: "传感器与控制: 车载传感器的认识及应用",
            chapter: "第2章 第5节",
            url: "/images/2.5认识传感器.png",
            link: "/answers/2/5",
          },
          {
            name: "传感器与控制: 小车巡线行驶",
            chapter: "第2章 第6节",
            url: "/images/颜色传感器与颜色巡线.png",
            link: "/answers/2/6",
          },
          {
            name: "传感器与控制: 小车测距行驶",
            chapter: "第2章 第7节",
            url: "/images/2.8竞速小车.png",
            link: "/answers/2/7",
          },
          {
            name: "传感器与控制: 复杂线路下小车的测距行驶",
            chapter: "第2章 第8节",
            url: "/images/测距传感器和避障行走.png",
            link: "/answers/2/8",
          },
          {
            name: "机器学习: 通过线性回归预测牧羊犬体重",
            chapter: "第3章 第1节",
            url: "/images/5.1线性回归模型.png",
            link: "/answers/3/1",
          },
          {
            name: "机器学习: 通过多项式回归预测牧羊犬体重",
            chapter: "第3章 第2节",
            url: "/images/5.2多项式回归模型.png",
            link: "/answers/3/2",
          },
          {
            name: "机器学习: 线性回归模型评估与测试集",
            chapter: "第3章 第3节",
            url: "/images/5.3线性回归模型评估与测试集合.png",
            link: "/answers/3/3",
          },
          {
            name: "机器学习: 线性分类预测性别",
            chapter: "第3章 第4节",
            url: "/images/5.5线性分类模型.png",
            link: "/answers/3/4",
          },
          {
            name: "机器学习: 利用身高和体重预测性别",
            chapter: "第3章 第5节",
            url: "/images/5.7多变量分类模型.png",
            link: "/answers/3/5",
          },
          {
            name: "机器学习: 利用感知器完成鸢尾花分类",
            chapter: "第3章 第6节",
            url: "/images/2-利用感知器完成鸢尾花分类.png",
            link: "/answers/3/6",
          },
          {
            name: "机器学习: 利用支持向量机完成鸢尾花分类",
            chapter: "第3章 第7节",
            url: "/images/2-利用SVM完成鸢尾花分类.png",
            link: "/answers/3/7",
          },
          {
            name: "机器学习: 分类器的测试与应用",
            chapter: "第3章 第8节",
            url: "/images/2-分类器的测试与应用.png",
            link: "/answers/3/8",
          },
          {
            name: "机器学习: 理解K均值算法",
            chapter: "第3章 第9节",
            url: "/images/6-相册中的人脸聚类：理解K值均算法.png",
            link: "/answers/3/9",
          },
          {
            name: "人工神经网络: 利用神经网络完成商区分类任务",
            chapter: "第4章 第1节",
            url: "/images/6.2深度学习-人工神经网络.png",
            link: "/answers/4/1",
          },
          {
            name: "人工神经网络: 基于身高预测体重",
            chapter: "第4章 第2节",
            url: "/images/6.3神经网络回归-基于身高预测体重.png",
            link: "/answers/4/2",
          },
          {
            name: "图像处理: 图像的像素和色彩",
            chapter: "第5章 第1节",
            url: "/images/4.1图像数据基础.png",
            link: "/answers/5/1",
          },
          {
            name: "图像处理: 图像的色彩变换",
            chapter: "第5章 第2节",
            url: "/images/4.2图像处理技术—色彩变换.png",
            link: "/answers/5/2",
          },
          {
            name: "图像处理: 图像特效的制作",
            chapter: "第5章 第3节",
            url: "/images/4.3图像处理技术—空间变换.png",
            link: "/answers/5/3",
          },
          {
            name: "图像处理: 图像扭曲",
            chapter: "第5章 第4节",
            url: "/images/4.4-表情包1-图像扭曲.png",
            link: "/answers/5/4",
          },
          {
            name: "图像处理: 人脸关键点检测",
            chapter: "第5章 第5节",
            url: "/images/4.5表情包2-人脸关键点检测.png",
            link: "/answers/5/5",
          },
          {
            name: "图像处理: 动态表情包制作",
            chapter: "第5章 第6节",
            url: "/images/4.6-表情包3-大项目：动态表情包制作.png",
            link: "/answers/5/6",
          },
          {
            name: "计算机视觉: 利用图像特征完成图像识别",
            chapter: "第6章 第1节",
            url: "/images/3-深度学习与图像识别：利用图像特征.png",
            link: "/answers/6/1",
          },
          {
            name: "计算机视觉: 利用深度神经网络完成图像分类",
            chapter: "第6章 第2节",
            url: "/images/3-深度学习与图像识别：利用深度神经网络完成图像分类.png",
            link: "/answers/6/2",
          },
          {
            name: "计算机视觉: 提取照片中的人脸特征",
            chapter: "第6章 第3节",
            url: "/images/6-相册中的人脸聚类：提取照片中的人脸特征.png",
            link: "/answers/6/3",
          },
          {
            name: "计算机视觉: 相册中的人脸聚类",
            chapter: "第6章 第4节",
            url: "/images/6-相册中的人脸聚类：相册中的K均聚类.png",
            link: "/answers/6/4",
          },
          {
            name: "计算机视觉: 理解视频中的光流",
            chapter: "第6章 第5节",
            url: "/images/5-视频理解：理解视频中的光流.png",
            link: "/answers/6/5",
          },
          {
            name: "计算机视觉: 利用光流直方图完成行为识别任务",
            chapter: "第6章 第6节",
            url: "/images/5-视频理解：利用光流直方图完成行为识别任务.png",
            link: "/answers/6/6",
          },
          {
            name: "计算机视觉: 用生成对抗网络生成明星图片",
            chapter: "第6章 第7节",
            url: "/images/8-计算机创作图画：用声称对抗网络生成明星图片.png",
            link: "/answers/6/7",
          },
          {
            name: "文本分析: 字符串和文本文件的读写",
            chapter: "第7章 第1节",
            url: "/images/7.1字符串和文本文件的读.png",
            link: "/answers/7/1",
          },
          {
            name: "文本分析: 字典和词频统计",
            chapter: "第7章 第2节",
            url: "/images/7.2分词和列表.png",
            link: "/answers/7/2",
          },
          {
            name: "文本分析: 课文文章特征提取",
            chapter: "第7章 第3节",
            url: "/images/7.4智能课文分析1.png",
            link: "/answers/7/3",
          },
          {
            name: "文本分析: 课文难度分类",
            chapter: "第7章 第4节",
            url: "/images/7.6智能课文分析3.png",
            link: "/answers/7/4",
          },
          {
            name: "文本分析: 提取文本特征",
            chapter: "第7章 第5节",
            url: "/images/7-文本理解：提取文本特征.png",
            link: "/answers/7/5",
          },
          {
            name: "文本分析: 发掘文本中的潜在主题",
            chapter: "第7章 第6节",
            url: "/images/7-文本理解：发掘文本中的潜在主题.png",
            link: "/answers/7/6",
          },
        ],
      },
      {
        cate: "第2章",
        items: [
          {
            name: "传感器与控制: 启动小车",
            chapter: "第2章 第1节",
            url: "/images/2.1你的专属小车.png",
            link: "/answers/2/1",
          },
          {
            name: "传感器与控制: 控制小车的方向",
            chapter: "第2章 第2节",
            url: "/images/2.2虚拟小车的转弯.png",
            link: "/answers/2/2",
          },
          {
            name: "传感器与控制: 控制小车通过U型赛道",
            chapter: "第2章 第3节",
            url: "/images/2.4通过U形赛道.png",
            link: "/answers/2/3",
          },
          {
            name: "传感器与控制: 控制小车行完成指定道路",
            chapter: "第2章 第4节",
            url: "/images/2.6重复任务与循环结构.png",
            link: "/answers/2/4",
          },
          {
            name: "传感器与控制: 车载传感器的认识及应用",
            chapter: "第2章 第5节",
            url: "/images/2.5认识传感器.png",
            link: "/answers/2/5",
          },
          {
            name: "传感器与控制: 小车巡线行驶",
            chapter: "第2章 第6节",
            url: "/images/颜色传感器与颜色巡线.png",
            link: "/answers/2/6",
          },
          {
            name: "传感器与控制: 小车测距行驶",
            chapter: "第2章 第7节",
            url: "/images/2.8竞速小车.png",
            link: "/answers/2/7",
          },
          {
            name: "传感器与控制: 复杂线路下小车的测距行驶",
            chapter: "第2章 第8节",
            url: "/images/测距传感器和避障行走.png",
            link: "/answers/2/8",
          },
        ],
      },
      {
        cate: "第3章",
        items: [
          {
            name: "机器学习: 通过线性回归预测牧羊犬体重",
            chapter: "第3章 第1节",
            url: "/images/5.1线性回归模型.png",
            link: "/answers/3/1",
          },
          {
            name: "机器学习: 通过多项式回归预测牧羊犬体重",
            chapter: "第3章 第2节",
            url: "/images/5.2多项式回归模型.png",
            link: "/answers/3/2",
          },
          {
            name: "机器学习: 线性回归模型评估与测试集",
            chapter: "第3章 第3节",
            url: "/images/5.3线性回归模型评估与测试集合.png",
            link: "/answers/3/3",
          },
          {
            name: "机器学习: 线性分类预测性别",
            chapter: "第3章 第4节",
            url: "/images/5.5线性分类模型.png",
            link: "/answers/3/4",
          },
          {
            name: "机器学习: 利用身高和体重预测性别",
            chapter: "第3章 第5节",
            url: "/images/5.7多变量分类模型.png",
            link: "/answers/3/5",
          },
          {
            name: "机器学习: 利用感知器完成鸢尾花分类",
            chapter: "第3章 第6节",
            url: "/images/2-利用感知器完成鸢尾花分类.png",
            link: "/answers/3/6",
          },
          {
            name: "机器学习: 利用支持向量机完成鸢尾花分类",
            chapter: "第3章 第7节",
            url: "/images/2-利用SVM完成鸢尾花分类.png",
            link: "/answers/3/7",
          },
          {
            name: "机器学习: 分类器的测试与应用",
            chapter: "第3章 第8节",
            url: "/images/2-分类器的测试与应用.png",
            link: "/answers/3/8",
          },
          {
            name: "机器学习: 理解K均值算法",
            chapter: "第3章 第9节",
            url: "/images/6-相册中的人脸聚类：理解K值均算法.png",
            link: "/answers/3/9",
          },
        ],
      },
      {
        cate: "第4章",
        items: [
          {
            name: "人工神经网络: 利用神经网络完成商区分类任务",
            chapter: "第4章 第1节",
            url: "/images/6.2深度学习-人工神经网络.png",
            link: "/answers/4/1",
          },
          {
            name: "人工神经网络: 基于身高预测体重",
            chapter: "第4章 第2节",
            url: "/images/6.3神经网络回归-基于身高预测体重.png",
            link: "/answers/4/2",
          },
        ],
      },
      {
        cate: "第5章",
        items: [
          {
            name: "图像处理: 图像的像素和色彩",
            chapter: "第5章 第1节",
            url: "/images/4.1图像数据基础.png",
            link: "/answers/5/1",
          },
          {
            name: "图像处理: 图像的色彩变换",
            chapter: "第5章 第2节",
            url: "/images/4.2图像处理技术—色彩变换.png",
            link: "/answers/5/2",
          },
          {
            name: "图像处理: 图像特效的制作",
            chapter: "第5章 第3节",
            url: "/images/4.3图像处理技术—空间变换.png",
            link: "/answers/5/3",
          },
          {
            name: "图像处理: 图像扭曲",
            chapter: "第5章 第4节",
            url: "/images/4.4-表情包1-图像扭曲.png",
            link: "/answers/5/4",
          },
          {
            name: "图像处理: 人脸关键点检测",
            chapter: "第5章 第5节",
            url: "/images/4.5表情包2-人脸关键点检测.png",
            link: "/answers/5/5",
          },
          {
            name: "图像处理: 动态表情包制作",
            chapter: "第5章 第6节",
            url: "/images/4.6-表情包3-大项目：动态表情包制作.png",
            link: "/answers/5/6",
          },
        ],
      },
      {
        cate: "第6章",
        items: [
          {
            name: "计算机视觉: 利用图像特征完成图像识别",
            chapter: "第6章 第1节",
            url: "/images/3-深度学习与图像识别：利用图像特征.png",
            link: "/answers/6/1",
          },
          {
            name: "计算机视觉: 利用深度神经网络完成图像分类",
            chapter: "第6章 第2节",
            url: "/images/3-深度学习与图像识别：利用深度神经网络完成图像分类.png",
            link: "/answers/6/2",
          },
          {
            name: "计算机视觉: 提取照片中的人脸特征",
            chapter: "第6章 第3节",
            url: "/images/6-相册中的人脸聚类：提取照片中的人脸特征.png",
            link: "/answers/6/3",
          },
          {
            name: "计算机视觉: 相册中的人脸聚类",
            chapter: "第6章 第4节",
            url: "/images/6-相册中的人脸聚类：相册中的K均聚类.png",
            link: "/answers/6/4",
          },
          {
            name: "计算机视觉: 理解视频中的光流",
            chapter: "第6章 第5节",
            url: "/images/5-视频理解：理解视频中的光流.png",
            link: "/answers/6/5",
          },
          {
            name: "计算机视觉: 利用光流直方图完成行为识别任务",
            chapter: "第6章 第6节",
            url: "/images/5-视频理解：利用光流直方图完成行为识别任务.png",
            link: "/answers/6/6",
          },
          {
            name: "计算机视觉: 用生成对抗网络生成明星图片",
            chapter: "第6章 第7节",
            url: "/images/8-计算机创作图画：用声称对抗网络生成明星图片.png",
            link: "/answers/6/7",
          },
        ],
      },
      {
        cate: "第7章",
        items: [
          {
            name: "文本分析: 字符串和文本文件的读写",
            chapter: "第7章 第1节",
            url: "/images/7.1字符串和文本文件的读.png",
            link: "/answers/7/1",
          },
          {
            name: "文本分析: 字典和词频统计",
            chapter: "第7章 第2节",
            url: "/images/7.2分词和列表.png",
            link: "/answers/7/2",
          },
          {
            name: "文本分析: 课文文章特征提取",
            chapter: "第7章 第3节",
            url: "/images/7.4智能课文分析1.png",
            link: "/answers/7/3",
          },
          {
            name: "文本分析: 课文难度分类",
            chapter: "第7章 第4节",
            url: "/images/7.6智能课文分析3.png",
            link: "/answers/7/4",
          },
          {
            name: "文本分析: 提取文本特征",
            chapter: "第7章 第5节",
            url: "/images/7-文本理解：提取文本特征.png",
            link: "/answers/7/5",
          },
          {
            name: "文本分析: 发掘文本中的潜在主题",
            chapter: "第7章 第6节",
            url: "/images/7-文本理解：发掘文本中的潜在主题.png",
            link: "/answers/7/6",
          },
        ],
      },
    ];
  },
});
