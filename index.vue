<script setup lang="ts">
import { data } from "./dist.data";
import { ElTabPane, ElIcon, ElTabs } from "element-plus";
import { CopyDocument, Paperclip } from "@element-plus/icons-vue";
</script>
<template>
  <div class="page">
    <div class="courseDiv">
      <img src="/images/course_default.png" alt="" />
      <div class="courseContent">
        <div class="title">人工智能基础导论</div>
        <div class="description"></div>
        <div>共 6 章 38 节</div>
      </div>
    </div>
    <div class="tabs">
      <el-tabs>
        <el-tab-pane
          :label="item.cate"
          v-for="(item, index) in data"
          :key="index"
        >
          <div class="body">
            <div class="container">
              <div v-for="(jitem, jindex) in item.items" :key="jindex">
                <a :href="jitem.link">
                  <div class="item">
                    <img :src="jitem.url" />
                    <div class="lable">
                      <div class="name">{{ jitem.name }}</div>
                      <div class="chapter">{{ jitem.chapter }}</div>
                      <div class="button">
                        <el-icon><CopyDocument /></el-icon>
                        <el-icon><Paperclip /></el-icon>
                      </div>
                    </div>
                  </div>
                </a>
              </div>
            </div>
          </div>
        </el-tab-pane>
      </el-tabs>
    </div>
  </div>
</template>
<style lang="scss">
.page {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-items: center;
  padding: 35px 35px 0;
  .courseDiv {
    width: 100%;
    margin-bottom: 30px;
    box-shadow: 0 2px 8px var(--mcitem-box-shadow);
    border-radius: 8px;
    display: flex;
    color: #999;
    img {
      width: 45%;
    }
    .courseContent {
      padding: 40px;
      .title {
        font-size: 26px;
        font-weight: 699;
        color: var(--mcitem-color);
        margin-bottom: 20px;
      }
    }
    @media (max-width: 460px) {
      .courseContent {
        padding: 0;
        padding-left: 30px;
        .title {
          font-size: 15px;
          margin-top: 10px;
        }
      }
    }
  }
  .tabs {
    width: 100%;
    .body {
      margin: 0 12px;
      margin-bottom: 20px;
      padding-top: 10px;
      .container {
        margin: 0 auto;
        display: grid;
        gap: 22px;
        grid-template-columns: 1fr 1fr;
        .item {
          display: grid;
          grid-template-columns: 120px 1fr;
          box-shadow: 0 2px 8px var(--mcitem-box-shadow);
          img {
            width: 100px;
            height: 100px;
            border-radius: 50%;
            margin: auto;
          }
          .lable {
            margin: 10px 10px 10px 0;
            .name {
              margin-bottom: 25px;
              color: var(--mcitem-color);
              font-size: 15px;
              font-weight: 699;
            }
            .chapter {
              font-size: 14px;
              color: #999;
              letter-spacing: 0.1em;
            }
            .button {
              margin-top: 10px;
            }
          }
        }
        .item:hover {
          .name {
            color: var(--mcitem-color);
          }
        }
      }
      @media (max-width: 460px) {
        .container {
          grid-template-columns: 1fr;
          .item {
            img {
              width: 88px;
              height: 88px;
            }
          }
        }
      }
    }
  }
}
</style>
