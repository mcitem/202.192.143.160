// ==UserScript==
// @name         商汤教育 / SenseStudy / 人工智能基础素养 / 202.192.143.160 允许复制
// @namespace    https://bbs.tampermonkey.net.cn/
// @version      0.2.6
// @description  商汤教育 / SenseStudy / 人工智能基础素养 / 202.192.143.160 允许复制工具、点击code控件可自动复制，若无效请尝试刷新页面
// @author       mcitem
// @match        https://202.192.143.160/student/experiment/*
// @match        https://csvpn.lingnan.edu.cn/https/77726476706e69737468656265737421a2a713d276693a1e2f5cdae2c90373/student/experiment/*
// ==/UserScript==

(async function () {
  "use strict";
  function use() {
    const elements = document.querySelectorAll(
      "[class*='ExpSteps_myCollapse']"
    );
    for (let i = 0; i < elements.length; i++) {
      elements[i].style.userSelect = "auto";
      const codes = elements[0].getElementsByTagName("pre");
      for (let i = 0; i < codes.length; i++) {
        let code = codes[i];
        if (!code.hasAttribute("data-copy-bound")) {
          code.addEventListener("click", function () {
            console.log(code.innerText);
            navigator.clipboard.writeText(code.innerText);
          });
          code.setAttribute("data-copy-bound", "true");
        }
      }
    }
  }
  window.addEventListener("load", function () {
    document.addEventListener("keydown", function (event) {
      if (event.ctrlKey && event.key === "r") {
        event.preventDefault();
        const buttons = document.querySelectorAll(
          "[class*='ExpRunControl_btn']"
        );
        buttons.forEach((button) => {
          button.click();
        });
      }
    });
  });
  setInterval(use, 1000);
})();
