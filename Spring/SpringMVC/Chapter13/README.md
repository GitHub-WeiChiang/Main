Chapter13 使用客製化標籤開發 JSP 程式
=====
* ### 開發人員分類參考
    * ### web designers: view 開發 (前端)。
    * ### web component developers: controller 開發 (後端)。
    * ### sudiness component developers: model 開發 (後端)。
* ### taglib 指示標籤
    * ### prefix 為標籤前置詞，用於區分標籤函示庫，核心 (core) 標籤函示庫慣用 c 表示。
    * ### uri 為對應關係。
* ### JSTL 核心標籤
    * ### ```<c:set>```: 儲存變數 (可指定範圍)。
    * ### ```<c:url>```: 提供 (得到)具有 URL-Rewriting 的 session 管理功能。
    * ### ```<c:out>```: 執行運算式並輸出結果。
    * ### ```<c:remove>```: 刪除指定範圍的變數。
    * ### ```<c:catch>```: 捕捉例外。
    * ### ```<c:if>```: 就是 if。
    * ### ```<c:choose>```: 作為下兩個標籤的父標籤。
    * ### ```<c:when>```: 等價於 if / else if。
    * ### ```<c:otherwise>```: 等價於 else。
    * ### ```<c:forEach>```: 重複結構。
    * ### ```<c:forTokens>```: 字串切割。
    * ### ```<c:import>```: 包含另一個 URL 內容到本頁。
    * ### ```<c:redirect>```: 頁面重導向。
    * ### ```<c:param>```: 新增參數到 request 中。
* ### JSTL 其它標籤函式庫
    * ### 核心功能 (c)
    * ### 格式化功能 (fmt)
    * ### XML 處理功能 (x)
    * ### 資料庫存取功能 (sql)
    * ### 其它功能 (fn)
<br />
