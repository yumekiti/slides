---
marp: true
title: サンプルスライド
paginate: true
theme: custom
---

# サンプルスライド

サブタイトル / 発表者名など

---

<!--
_class: agenda
-->

## Agenda

1. OverView: このテンプレートについて
2. Section: 画像 + テキストのレイアウト例
3. Table: 表組みの例
4. Note: 補足・注意書きの例
5. Support: 参考リンクの例

---

`OverView`

## このテンプレートについて

### 概要

このディレクトリは、新しいスライドを作成する際のベースとして利用できるサンプルです。
`umbrella/JA` の構成を参考に、Marp + `style.css`（`custom` テーマ）で
共通して使えるレイアウトパターンをまとめています。

コピーして中身を書き換えるだけで、新しいスライドをすぐに作成できます。

---

`Section`

## 画像 + テキストのレイアウト例

<div class="columns ratio-6-4">
  <div>

### 左カラム

`columns ratio-6-4` と `card` クラスを組み合わせると、
左にテキスト、右に画像・図解を配置するレイアウトが作れます。

- 箇条書きもそのまま使えます
- カラム比率は `ratio-6-4` / `ratio-5-5` から選択可能です

  </div>
  <div class="card">

<img src="../assets/placeholder.svg" class="cover-image" />
<div class="text-center"> 画像・図解を配置する例 </div>

  </div>
</div>

---

`Table`

## 表組みの例

| 項目       | 内容                     | 補足                 |
| ---------- | ------------------------ | -------------------- |
| タイトル   | スライド冒頭の見出し     | H1 で記述            |
| Agenda     | 目次スライド             | `_class: agenda`     |
| セクション | 各トピックの内容         | カラム / カード活用  |
| 表         | 情報整理・比較           | Markdown のテーブル  |

---

`Note`

## 補足・注意書きの例

> 補足事項や注意書きは blockquote（`>`）で記述すると、
> グレー背景の枠で強調表示されます。

- 前提条件や既知の制約を書く際に利用してください
- 長文になりすぎないよう簡潔にまとめるのがおすすめです

---

`Support`

## 参考リンクの例

- 本リポジトリの参考コマンド: [Refarence.md](../../Refarence.md)
- 共通スタイル: [style.css](../../style.css)
- 参考ディレクトリ: [umbrella/JA](../../umbrella/JA/)

---
