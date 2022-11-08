樣板方法模式 TemplateMethodPattern
=====
### 將一個演算法的骨架定義在一個方法中，而演算法本身會用到的一些方法，則是定義在次類別中。樣板方法讓次類別在不改變演算法架構的情況下，重新定義演算法中的某些步驟。
<br />

樣板方法模式應用
=====
* ### compareTo(Object object) 方法的覆寫
<br />

掛鉤應用 Hook
=====
* ### Swing 視窗程式中可覆寫的 paint() 方法 （來自於 JFrame 類別）
* ### Applet 類別中可覆寫的 init()、start()、stop()、destroy()、paint() 方法 （來自於 Applet 類別）