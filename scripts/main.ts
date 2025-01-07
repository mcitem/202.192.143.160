import data from "./src.data";
import * as fs from "fs";
import * as path from "path";
import * as prettier from "prettier";

const DOWNLOAD = false;
process.env.NODE_TLS_REJECT_UNAUTHORIZED = "0";

let cates: string[] = [];
let dist: {
  cate: string;
  items: {
    name: string;
    chapter: string;
  }[];
}[] = [
  {
    cate: "全部",
    items: [],
  },
];
let configs: {
  text: string;
  collapsed: boolean;
  items: {
    text: string;
    link: string;
  }[];
}[] = [];

const distDir = path.join(__dirname, "dist");
if (!fs.existsSync(distDir)) {
  fs.mkdirSync(distDir);
}

data.forEach((item) => {
  const url = "https://202.192.143.160" + encodeURI(item.iconPath);
  const match = item.iconPath.match(/\/([^/]+)$/);
  const name = match ? match[1] : "";

  if (!cates.includes(item.chapter)) {
    dist.push({
      cate: `第${item.chapter}章`,
      items: [],
    });
    configs.push({
      text: `第${item.chapter}章: ${item.chapterName}`,
      collapsed: true,
      items: [],
    });
    cates.push(item.chapter);
  }
  const index = cates.indexOf(item.chapter);

  const child = {
    name: `${item.chapterName}: ${item.name}`,
    chapter: `第${item.chapter}章 第${item.quarter}节`,
    url: "/images/" + name,
    link: `/answers/${item.chapter}/${item.quarter}`,
  };

  dist[index + 1].items.push(child);
  dist[0].items.push(child);
  if (DOWNLOAD) {
    fetch(url).then(async (res) => {
      console.log(name, res.status);
      const buffer = Buffer.from(await res.arrayBuffer());
      fs.writeFileSync(path.join(distDir, name), buffer);
    });
  }

  configs[index].items.push({
    text: `第${item.quarter}节: ${item.name}`,
    link: `/answers/${item.chapter}/${item.quarter}`,
  });
});
prettier
  .format(`export default ${JSON.stringify(dist)}`, {
    parser: "typescript",
  })
  .then((code) => {
    fs.writeFileSync(path.join(distDir, "dist.data.ts"), code);
  });
prettier.format(JSON.stringify(configs), { parser: "json" }).then((code) => {
  fs.writeFileSync(path.join(distDir, "config.json"), code);
});
