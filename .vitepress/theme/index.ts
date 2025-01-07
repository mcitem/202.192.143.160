// https://vitepress.dev/guide/custom-theme
import { h } from "vue";
import type { Theme } from "vitepress";
import DefaultTheme from "vitepress/theme";
import { ID_INJECTION_KEY } from "element-plus";
import { ZINDEX_INJECTION_KEY } from "element-plus";
import "element-plus/dist/index.css";
import "element-plus/theme-chalk/dark/css-vars.css";
import "./style.scss";
export default {
  extends: DefaultTheme,
  Layout: () => {
    return h(DefaultTheme.Layout, null, {
      // https://vitepress.dev/guide/extending-default-theme#layout-slots
    });
  },
  enhanceApp({ app, router, siteData }) {
    app.provide(ID_INJECTION_KEY, {
      prefix: 1024,
      current: 0,
    });
    app.provide(ZINDEX_INJECTION_KEY, { current: 0 });
    // ...
  },
} satisfies Theme;
