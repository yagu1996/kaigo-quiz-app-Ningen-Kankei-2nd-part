import streamlit as st
import datetime
import html

# ページ設定
st.set_page_config(
    page_title="No.1 人間関係とコミュニケーション 練習問題 b後半",
    page_icon="📝",
    layout="centered"
)

# 明朝体およびルビ表示用カスタムCSS
st.markdown("""
<style>
  * {
    font-family: "Hiragino Mincho ProN", "Yu Mincho", "MS Mincho", "Source Han Serif", serif !important;
  }
  ruby { ruby-align: center; }
  rt { font-size: 0.55em; font-weight: normal; line-height: 1; }
  .chapter-header {
    background-color: #1e3a8a;
    color: white;
    padding: 8px 14px;
    border-radius: 4px;
    font-weight: bold;
    font-size: 1.05rem;
    margin: 22px 0 10px 0;
  }
  .section-header {
    color: #334155;
    font-weight: bold;
    font-size: 0.95rem;
    border-bottom: 2px dashed #94a3b8;
    padding-bottom: 4px;
    margin: 16px 0 10px 0;
  }
  .q-title {
    font-size: 1.02rem;
    font-weight: bold;
    margin-bottom: 8px;
    color: #0f172a;
    line-height: 1.6;
  }
  .opt-item {
    margin-left: 20px;
    font-size: 0.93rem;
    margin-bottom: 5px;
    line-height: 1.5;
  }
</style>
""", unsafe_allow_html=True)

# タイトル表示
st.markdown("""
<h2 style='text-align: center; border-bottom: 2px solid #1e3a8a; padding-bottom: 8px; color: #1e3a8a;'>
No.2 <ruby>人<rt>にん</rt>間<rt>げん</rt>関<rt>かん</rt>係<rt>けい</rt></ruby>とコミュニケーション <ruby>練<rt>れん</rt>習<rt>しゅう</rt>問<rt>もん</rt>題<rt>だい</rt></ruby> b<ruby>後半<rt>こうはん</rt></ruby>
</h2>
<p style='text-align: center; font-size: 0.9rem; color: #475569;'>
Google Classroom 課題提出対応Webアプリ（全25問・4択式）
</p>
""", unsafe_allow_html=True)

# 学生情報入力カード
st.markdown("### 👤 学生情報の入力")
col1, col2, col3 = st.columns([1, 1, 1.5])
with col1:
    s_class = st.text_input("組（クラス名）", placeholder="例: 1年A組")
with col2:
    s_id = st.text_input("学籍番号", placeholder="例: 20260101")
with col3:
    s_name = st.text_input("氏名", placeholder="例: 山田 太郎")

# 設問データ（全25問・完全ルビ付き）
questions = [
  {
    "num": 1,
    "chapter": "<ruby>第<rt>だい</rt></ruby>2<ruby>章<rt>しょう</rt></ruby> <ruby>人<rt>にん</rt>間<rt>げん</rt>関<rt>かん</rt>係<rt>けい</rt></ruby>とコミュニケーション",
    "section": "<ruby>第<rt>だい</rt></ruby>1<ruby>節<rt>せつ</rt></ruby> <ruby>人<rt>にん</rt>間<rt>げん</rt></ruby>と<ruby>人<rt>にん</rt>間<rt>げん</rt>関<rt>かん</rt>係<rt>けい</rt></ruby>（3 <ruby>発<rt>はつ</rt>達<rt>たつ</rt>心<rt>しん</rt>理<rt>り</rt>学<rt>がく</rt></ruby>からみた<ruby>人<rt>にん</rt>間<rt>げん</rt>関<rt>かん</rt>係<rt>けい</rt></ruby>）",
    "stem": "1. エリクソンの<ruby>発<rt>はつ</rt>達<rt>たつ</rt>段<rt>だん</rt>階<rt>かい</rt>説<rt>せつ</rt></ruby>において、<ruby>乳<rt>にゅう</rt>児<rt>じ</rt>期<rt>き</rt></ruby>（<ruby>生<rt>せい</rt>後<rt>ご</rt></ruby>〜2<ruby>歳<rt>さい</rt></ruby>ごろ）の<ruby>発<rt>はつ</rt>達<rt>たつ</rt>課<rt>か</rt>題<rt>だい</rt></ruby>と<ruby>危<rt>き</rt>機<rt>き</rt></ruby>の<ruby>組<rt>く</rt></ruby>み<ruby>合<rt>あ</rt></ruby>わせとして、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "1. <ruby>自<rt>じ</rt>律<rt>りつ</rt>性<rt>せい</rt></ruby>の<ruby>獲<rt>かく</rt>得<rt>とく</rt></ruby> ― <ruby>恥<rt>はじ</rt></ruby>・<ruby>疑<rt>ぎ</rt>惑<rt>わく</rt></ruby>",
      "2. <ruby>基<rt>き</rt>本<rt>ほん</rt>的<rt>てき</rt>信<rt>しん</rt>頼<rt>らい</rt></ruby>の<ruby>獲<rt>かく</rt>得<rt>とく</rt></ruby> ― <ruby>不<rt>ふ</rt>信<rt>しん</rt></ruby>",
      "3. <ruby>勤<rt>きん</rt>勉<rt>べん</rt>性<rt>せい</rt></ruby>の<ruby>獲<rt>かく</rt>得<rt>とく</rt></ruby> ― <ruby>劣<rt>れっ</rt>とう<rt>とう</rt>感<rt>かん</rt></ruby>",
      "4. <ruby>同<rt>どう</rt>一<rt>いつ</rt>性<rt>せい</rt></ruby>の<ruby>獲<rt>かく</rt>得<rt>とく</rt></ruby> ― <ruby>同<rt>どう</rt>一<rt>いつ</rt>性<rt>せい</rt>拡<rt>かく</rt>散<rt>さん</rt></ruby>"
    ],
    "answer": 2,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 2（<ruby>基<rt>き</rt>本<rt>ほん</rt>的<rt>てき</rt>信<rt>しん</rt>頼<rt>らい</rt></ruby>の<ruby>獲<rt>かく</rt>得<rt>とく</rt></ruby> ― <ruby>不<rt>ふ</rt>信<rt>しん</rt></ruby>）"
  },
  {
    "num": 2,
    "stem": "2. エリクソンの<ruby>発<rt>はつ</rt>達<rt>たつ</rt>段<rt>だん</rt>階<rt>かい</rt>説<rt>せつ</rt></ruby>において、<ruby>幼<rt>よう</rt>児<rt>じ</rt>期<rt>き</rt>前<rt>ぜん</rt>期<rt>き</rt></ruby>（4<ruby>歳<rt>さい</rt></ruby>ごろまで）にしつけなどを<ruby>通<rt>つう</rt></ruby>して<ruby>身<rt>しん</rt>体<rt>たい</rt></ruby>をコントロールすることを<ruby>学<rt>がく</rt>習<rt>しゅう</rt></ruby>する<ruby>発<rt>はつ</rt>達<rt>たつ</rt>課<rt>か</rt>題<rt>だい</rt></ruby>として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "1. <ruby>自<rt>じ</rt>律<rt>りつ</rt>性<rt>せい</rt></ruby>の<ruby>獲<rt>かく</rt>得<rt>とく</rt></ruby>",
      "2. <ruby>自<rt>じ</rt>主<rt>しゅ</rt>性<rt>せい</rt></ruby>の<ruby>獲<rt>かく</rt>得<rt>とく</rt></ruby>",
      "3. <ruby>親<rt>しん</rt>密<rt>みつ</rt>性<rt>せい</rt></ruby>の<ruby>獲<rt>かく</rt>得<rt>とく</rt></ruby>",
      "4. <ruby>生<rt>せい</rt>殖<rt>しょく</rt>性<rt>せい</rt></ruby>の<ruby>獲<rt>かく</rt>得<rt>とく</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>自<rt>じ</rt>律<rt>りつ</rt>性<rt>せい</rt></ruby>の<ruby>獲<rt>かく</rt>得<rt>とく</rt></ruby>）"
  },
  {
    "num": 3,
    "stem": "3. <ruby>乳<rt>にゅう</rt>幼<rt>よう</rt>児<rt>じ</rt>期<rt>き</rt></ruby>に<ruby>子<rt>こ</rt></ruby>どもと<ruby>養<rt>よう</rt>育<rt>いく</rt>者<rt>しゃ</rt></ruby>との<ruby>間<rt>あいだ</rt></ruby>に<ruby>形<rt>けい</rt>成<rt>せい</rt></ruby>される<ruby>情<rt>じょう</rt>緒<rt>ちょ</rt>的<rt>てき</rt></ruby>な<ruby>絆<rt>きずな</rt></ruby>を<ruby>指<rt>さ</rt></ruby>し、その<ruby>後<rt>ご</rt></ruby>の<ruby>人<rt>にん</rt>間<rt>げん</rt>関<rt>かん</rt>係<rt>けい</rt></ruby>の<ruby>基<rt>き</rt>礎<rt>そ</rt></ruby>（<ruby>内<rt>ない</rt>的<rt>てき</rt></ruby>ワーキングモデル）になるとボウルビィが<ruby>指<rt>し</rt>摘<rt>てき</rt></ruby>した<ruby>概<rt>がい</rt>念<rt>ねん</rt></ruby>として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "1. アイデンティティ",
      "2. <ruby>愛<rt>あい</rt>着<rt>ちゃく</rt></ruby>（アタッチメント）",
      "3. パーソナリティ",
      "4. ソーシャルスキル"
    ],
    "answer": 2,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 2（<ruby>愛<rt>あい</rt>着<rt>ちゃく</rt></ruby>（アタッチメント））"
  },
  {
    "num": 4,
    "stem": "4. トマスらによる<ruby>乳<rt>にゅう</rt>児<rt>じ</rt></ruby>の<ruby>気<rt>き</rt>質<rt>しつ</rt>分<rt>ぶん</rt>類<rt>るい</rt></ruby>において、「<ruby>規<rt>き</rt>則<rt>そく</rt>的<rt>てき</rt></ruby>だが<ruby>活<rt>かつ</rt>動<rt>どう</rt>水<rt>すい</rt>準<rt>じゅん</rt></ruby>が<ruby>低<rt>ひく</rt></ruby>く、<ruby>新<rt>あたら</rt></ruby>しい<ruby>状<rt>じょう</rt>況<rt>きょう</rt></ruby>への<ruby>適<rt>てき</rt>応<rt>おう</rt></ruby>に<ruby>時<rt>じ</rt>間<rt>かん</rt></ruby>がかかる」タイプとして、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "1. <ruby>扱<rt>あつか</rt></ruby>いやすい<ruby>子<rt>こ</rt></ruby>（Easy children）",
      "2. <ruby>扱<rt>あつか</rt></ruby>いにくい<ruby>子<rt>こ</rt></ruby>（Difficult children）",
      "3. エンジンがかかりにくい<ruby>子<rt>こ</rt></ruby>（Slow to warm up）",
      "4. <ruby>平<rt>へい</rt>均<rt>きん</rt>的<rt>てき</rt></ruby>な<ruby>子<rt>こ</rt></ruby>（Average children）"
    ],
    "answer": 3,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 3（エンジンがかかりにくい<ruby>子<rt>こ</rt></ruby>（Slow to warm up））"
  },
  {
    "num": 5,
    "section": "<ruby>第<rt>だい</rt></ruby>1<ruby>節<rt>せつ</rt></ruby> <ruby>人<rt>にん</rt>間<rt>げん</rt></ruby>と<ruby>人<rt>にん</rt>間<rt>げん</rt>関<rt>かん</rt>係<rt>けい</rt></ruby>（4 <ruby>社<rt>しゃ</rt>会<rt>かい</rt>心<rt>しん</rt>理<rt>り</rt>学<rt>がく</rt></ruby>からみた<ruby>人<rt>にん</rt>間<rt>げん</rt>関<rt>かん</rt>係<rt>けい</rt></ruby>）",
    "stem": "5. <ruby>他<rt>た</rt>者<rt>しゃ</rt></ruby>がある<ruby>側<rt>そく</rt>面<rt>めん</rt></ruby>で<ruby>望<rt>のぞ</rt></ruby>ましい（あるいは<ruby>望<rt>のぞ</rt></ruby>ましくない）<ruby>特<rt>とく</rt>徴<rt>ちょう</rt></ruby>を<ruby>持<rt>も</rt></ruby>っていると、その<ruby>評<rt>ひょう</rt>価<rt>か</rt></ruby>を<ruby>人<rt>じん</rt>物<rt>ぶつ</rt>全<rt>ぜん</rt>体<rt>たい</rt></ruby>にまで<ruby>広<rt>ひろ</rt></ruby>げてしまう<ruby>対<rt>たい</rt>人<rt>じん</rt>認<rt>にん</rt>知<rt>ち</rt></ruby>の<ruby>傾<rt>けい</rt>向<rt>こう</rt></ruby>として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "1. ステレオタイプ",
      "2. ハロー<ruby>効<rt>こう</rt>果<rt>か</rt></ruby>（<ruby>光<rt>こう</rt>背<rt>はい</rt>効<rt>こう</rt>果<rt>か</rt></ruby>）",
      "3. <ruby>初<rt>しょ</rt>頭<rt>とう</rt>効<rt>こう</rt>果<rt>か</rt></ruby>",
      "4. ピグマリオン<ruby>効<rt>こう</rt>果<rt>か</rt></ruby>"
    ],
    "answer": 2,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 2（ハロー<ruby>効<rt>こう</rt>果<rt>か</rt></ruby>（<ruby>光<rt>こう</rt>背<rt>はい</rt>効<rt>こう</rt>果<rt>か</rt></ruby>））"
  },
  {
    "num": 6,
    "stem": "6. <ruby>特<rt>とく</rt>定<rt>てい</rt></ruby>の<ruby>集<rt>しゅう</rt>団<rt>だん</rt></ruby>やそのメンバーに<ruby>対<rt>たい</rt></ruby>して、「<ruby>男<rt>だん</rt>性<rt>せい</rt></ruby>なら〜」「<ruby>高<rt>こう</rt>齢<rt>れい</rt>者<rt>しゃ</rt></ruby>は〜」のように<ruby>過<rt>か</rt>度<rt>ど</rt></ruby>に<ruby>一<rt>いっ</rt>般<rt>ぱん</rt>化<rt>か</rt></ruby>された<ruby>固<rt>こ</rt>定<rt>てい</rt>的<rt>てき</rt></ruby>な<ruby>見<rt>み</rt>方<rt>かた</rt></ruby>をする<ruby>認<rt>にん</rt>知<rt>ち</rt></ruby>の<ruby>傾<rt>けい</rt>向<rt>こう</rt></ruby>として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "1. ステレオタイプ",
      "2. <ruby>集<rt>しゅう</rt>団<rt>だん</rt>凝<rt>ぎょう</rt>集<rt>しゅう</rt>性<rt>せい</rt></ruby>",
      "3. <ruby>自<rt>じ</rt>己<rt>こ</rt>覚<rt>かく</rt>知<rt>ち</rt></ruby>",
      "4. <ruby>同<rt>どう</rt>調<rt>ちょう</rt>行<rt>こう</rt>動<rt>どう</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（ステレオタイプ）"
  },
  {
    "num": 7,
    "stem": "7. アッシュ（Asch）による<ruby>直<rt>ちょく</rt>線<rt>せん</rt></ruby>の<ruby>長<rt>なが</rt></ruby>さを<ruby>判<rt>はん</rt>定<rt>てい</rt></ruby>する<ruby>実<rt>じっ</rt>験<rt>けん</rt></ruby>で<ruby>明<rt>あき</rt></ruby>らかにされた、<ruby>集<rt>しゅう</rt>団<rt>だん</rt></ruby>の<ruby>多<rt>た</rt>数<rt>すう</rt>派<rt>は</rt></ruby>の<ruby>意<rt>い</rt>見<rt>けん</rt></ruby>に<ruby>合<rt>あ</rt></ruby>わせて<ruby>自<rt>じ</rt>分<rt>ぶん</rt></ruby>の<ruby>判<rt>はん</rt>断<rt>だん</rt></ruby>を<ruby>変<rt>へん</rt>化<rt>か</rt></ruby>させてしまう<ruby>現<rt>げん</rt>象<rt>しょう</rt></ruby>として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "1. <ruby>集<rt>しゅう</rt>団<rt>だん</rt>浅<rt>せん</rt>慮<rt>りょ</rt></ruby>",
      "2. <ruby>同<rt>どう</rt>調<rt>ちょう</rt>行<rt>こう</rt>動<rt>どう</rt></ruby>",
      "3. <ruby>内<rt>ない</rt>集<rt>しゅう</rt>団<rt>だん</rt>バイアス</ruby>",
      "4. リスキーシフト"
    ],
    "answer": 2,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 2（<ruby>同<rt>どう</rt>調<rt>ちょう</rt>行<rt>こう</rt>動<rt>どう</rt></ruby>）"
  },
  {
    "num": 8,
    "stem": "8. <ruby>自<rt>じ</rt>分<rt>ぶん</rt></ruby>が<ruby>所<rt>しょ</rt>属<rt>ぞく</rt></ruby>している<ruby>集<rt>しゅう</rt>団<rt>だん</rt></ruby>（<ruby>内<rt>ない</rt>集<rt>しゅう</rt>団<rt>だん</rt></ruby>）に<ruby>対<rt>たい</rt></ruby>して<ruby>好<rt>こう</rt>意<rt>い</rt>的<rt>てき</rt></ruby>な<ruby>態<rt>たい</rt>度<rt>ど</rt></ruby>をとる<ruby>いっ<rt>いっ</rt>ぽう<rt>ぽう</rt></ruby>で、<ruby>所<rt>しょ</rt>属<rt>ぞく</rt></ruby>していない<ruby>外<rt>がい</rt>集<rt>しゅう</rt>団<rt>だん</rt></ruby>に<ruby>対<rt>たい</rt></ruby>して<ruby>差<rt>さ</rt>別<rt>べつ</rt>的<rt>てき</rt></ruby>な<ruby>態<rt>たい</rt>度<rt>ど</rt></ruby>をとってしまう<ruby>傾<rt>けい</rt>向<rt>こう</rt></ruby>として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "1. <ruby>内<rt>ない</rt>集<rt>しゅう</rt>団<rt>だん</rt>バイアス</ruby>（<ruby>内<rt>ない</rt>集<rt>しゅう</rt>団<rt>だん</rt>びいき</ruby>）",
      "2. <ruby>社<rt>しゃ</rt>会<rt>かい</rt>的<rt>てき</rt>促<rt>そく</rt>進<rt>しん</rt></ruby>",
      "3. <ruby>傍<rt>ぼう</rt>観<rt>かん</rt>者<rt>しゃ</rt>効<rt>こう</rt>果<rt>か</rt></ruby>",
      "4. <ruby>自<rt>じ</rt>己<rt>こ</rt>奉<rt>ほう</rt>仕<rt>し</rt>バイアス</ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>内<rt>ない</rt>集<rt>しゅう</rt>団<rt>だん</rt>バイアス</ruby>（<ruby>内<rt>ない</rt>集<rt>しゅう</rt>団<rt>だん</rt>びいき</ruby>））"
  },
  {
    "num": 9,
    "section": "<ruby>第<rt>だい</rt></ruby>1<ruby>節<rt>せつ</rt></ruby> <ruby>人<rt>にん</rt>間<rt>げん</rt></ruby>と<ruby>人<rt>にん</rt>間<rt>げん</rt>関<rt>かん</rt>係<rt>けい</rt></ruby>（5 <ruby>人<rt>にん</rt>間<rt>げん</rt>関<rt>かん</rt>係<rt>けい</rt></ruby>とストレス）",
    "stem": "9. ラザルスらの<ruby>認<rt>にん</rt>知<rt>ち</rt>的<rt>てき</rt>評<rt>ひょう</rt>価<rt>か</rt>モデルにおいて、<ruby>直<rt>ちょく</rt>面<rt>めん</rt></ruby>した<ruby>出<rt>で</rt>来<rt>き</rt>事<rt>ごと</rt></ruby>に<ruby>対<rt>たい</rt></ruby>して「<ruby>自<rt>じ</rt>分<rt>ぶん</rt></ruby>にとってどのような<ruby>対<rt>たい</rt>処<rt>しょ</rt></ruby>が<ruby>可<rt>か</rt>能<rt>のう</rt></ruby>か」を<ruby>評<rt>ひょう</rt>価<rt>か</rt></ruby>する<ruby>段<rt>だん</rt>階<rt>かい</rt></ruby>として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "1. <ruby>一<rt>いち</rt>次<rt>じ</rt>評<rt>ひょう</rt>価<rt>か</rt></ruby>",
      "2. <ruby>二<rt>に</rt>次<rt>じ</rt>評<rt>ひょう</rt>価<rt>か</rt></ruby>",
      "3. <ruby>再<rt>さい</rt>評<rt>ひょう</rt>価<rt>か</rt></ruby>",
      "4. <ruby>結<rt>けっ</rt>果<rt>か</rt>評<rt>ひょう</rt>価<rt>か</rt></ruby>"
    ],
    "answer": 2,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 2（<ruby>二<rt>に</rt>次<rt>じ</rt>評<rt>ひょう</rt>価<rt>か</rt></ruby>）"
  },
  {
    "num": 10,
    "stem": "10. フリードマンらが<ruby>提<rt>てい</rt>唱<rt>しょう</rt></ruby>した、<ruby>高<rt>たか</rt></ruby>い<ruby>目<rt>もく</rt>的<rt>てき</rt>意<rt>い</rt>識<rt>しき</rt></ruby>をもち、<ruby>時<rt>じ</rt>間<rt>かん</rt></ruby>に<ruby>追<rt>お</rt></ruby>われ<ruby>競<rt>きょう</rt>争<rt>そう</rt>心<rt>しん</rt></ruby>が<ruby>強<rt>つよ</rt></ruby>く<ruby>攻<rt>こう</rt>撃<rt>げき</rt>的<rt>てき</rt></ruby>で、<ruby>冠<rt>かん</rt>状<rt>じょう</rt>動<rt>どう</rt>脈<rt>みゃく</rt>性<rt>せい</rt>疾<rt>しっ</rt>患<rt>かん</rt></ruby>を<ruby>起<rt>お</rt></ruby>こしやすい<ruby>行<rt>こう</rt>動<rt>どう</rt>様<rt>よう</rt>式<rt>しき</rt></ruby>として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "1. タイプA<ruby>行<rt>こう</rt>動<rt>どう</rt>パターン</ruby>",
      "2. タイプB<ruby>行<rt>こう</rt>動<rt>どう</rt>パターン</ruby>",
      "3. タイプC<ruby>行<rt>こう</rt>動<rt>どう</rt>パターン</ruby>",
      "4. タイプD<ruby>行<rt>こう</rt>動<rt>どう</rt>パターン</ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（タイプA<ruby>行<rt>こう</rt>動<rt>どう</rt>パターン</ruby>）"
  },
  {
    "num": 11,
    "stem": "11. ストレス<ruby>対<rt>たい</rt>処<rt>しょ</rt>行<rt>こう</rt>動<rt>どう</rt></ruby>（コーピング）のうち、<ruby>運<rt>うん</rt>動<rt>どう</rt></ruby>や<ruby>音<rt>おん</rt>楽<rt>がく</rt>鑑<rt>かん</rt>賞<rt>しょう</rt></ruby>、<ruby>気<rt>き</rt>分<rt>ぶん</rt>転<rt>てん</rt>換<rt>かん</rt></ruby>などによって、<ruby>引<rt>ひ</rt></ruby>き<ruby>起<rt>お</rt></ruby>こされたストレス<ruby>反<rt>はん</rt>応<rt>のう</rt></ruby>そのものを<ruby>統<rt>とう</rt>制<rt>せい</rt></ruby>・<ruby>軽<rt>けい</rt>減<rt>げん</rt></ruby>しようとする<ruby>方<rt>ほう</rt>法<rt>ほう</rt></ruby>として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "1. <ruby>問<rt>もん</rt>題<rt>だい</rt>焦<rt>しょう</rt>点<rt>てん</rt>型<rt>がた</rt></ruby>コーピング",
      "2. <ruby>情<rt>じょう</rt>動<rt>どう</rt>焦<rt>しょう</rt>点<rt>てん</rt>型<rt>がた</rt></ruby>コーピング",
      "3. <ruby>認<rt>にん</rt>知<rt>ち</rt>的<rt>てき</rt>再<rt>さい</rt>評<rt>ひょう</rt>価<rt>か</rt></ruby>",
      "4. <ruby>防<rt>ぼう</rt>衛<rt>えい</rt>機<rt>き</rt>制<rt>せい</rt></ruby>"
    ],
    "answer": 2,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 2（<ruby>情<rt>じょう</rt>動<rt>どう</rt>焦<rt>しょう</rt>点<rt>てん</rt>型<rt>がた</rt></ruby>コーピング）"
  },
  {
    "num": 12,
    "stem": "12. <ruby>周<rt>しゅう</rt>囲<rt>い</rt></ruby>からのソーシャル・サポートの<ruby>分<rt>ぶん</rt>類<rt>るい</rt></ruby>のうち、<ruby>共<rt>きょう</rt>感<rt>かん</rt></ruby>や<ruby>慰<rt>なぐさ</rt></ruby>め、<ruby>励<rt>はげ</rt></ruby>ましなどによって<ruby>精<rt>せい</rt>神<rt>しん</rt>的<rt>てき</rt></ruby>な<ruby>支<rt>ささ</rt></ruby>えを<ruby>提<rt>てい</rt>供<rt>きょう</rt></ruby>する<ruby>支<rt>し</rt>援<rt>えん</rt></ruby>として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "1. <ruby>情<rt>じょう</rt>報<rt>ほう</rt>的<rt>てき</rt></ruby>サポート",
      "2. <ruby>道<rt>どう</rt>具<rt>ぐ</rt>的<rt>てき</rt></ruby>サポート",
      "3. <ruby>情<rt>じょう</rt>緒<rt>ちょ</rt>的<rt>てき</rt></ruby>サポート",
      "4. <ruby>評<rt>ひょう</rt>価<rt>か</rt>的<rt>てき</rt></ruby>サポート"
    ],
    "answer": 3,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 3（<ruby>情<rt>じょう</rt>緒<rt>ちょ</rt>的<rt>てき</rt></ruby>サポート）"
  },
  {
    "num": 13,
    "section": "<ruby>第<rt>だい</rt></ruby>2<ruby>節<rt>せつ</rt></ruby> <ruby>対<rt>たい</rt>人<rt>じん</rt>関<rt>かん</rt>係<rt>けい</rt></ruby>におけるコミュニケーション",
    "stem": "13. コミュニケーション（communication）の<ruby>語<rt>ご</rt>源<rt>げん</rt></ruby>となったラテン<ruby>語<rt>ご</rt></ruby>が<ruby>持<rt>も</rt></ruby>つ<ruby>本<rt>ほん</rt>来<rt>らい</rt></ruby>の<ruby>意<rt>い</rt>味<rt>み</rt></ruby>として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "1. 「<ruby>支<rt>し</rt>配<rt>はい</rt></ruby>する」または「<ruby>命<rt>めい</rt>令<rt>れい</rt></ruby>する」",
      "2. 「<ruby>共<rt>きょう</rt>有<rt>ゆう</rt></ruby>する」または「<ruby>共<rt>きょう</rt>通<rt>つう</rt>項<rt>こう</rt></ruby>をつくる」",
      "3. 「<ruby>孤<rt>こ</rt>立<rt>りつ</rt></ruby>を<ruby>防<rt>ふせ</rt></ruby>ぐ」または「<ruby>救<rt>きゅう</rt>済<rt>さい</rt></ruby>する」",
      "4. 「<ruby>説<rt>せっ</rt>得<rt>とく</rt></ruby>する」または「<ruby>誘<rt>ゆう</rt>導<rt>どう</rt></ruby>する」"
    ],
    "answer": 2,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 2（「<ruby>共<rt>きょう</rt>有<rt>ゆう</rt></ruby>する」または「<ruby>共<rt>きょう</rt>通<rt>つう</rt>項<rt>こう</rt></ruby>をつくる」）"
  },
  {
    "num": 14,
    "stem": "14. <ruby>言<rt>げん</rt>語<rt>ご</rt></ruby>や<ruby>身<rt>み</rt>振<rt>ぶ</rt></ruby>りなど、あるものを<ruby>象<rt>しょう</rt>ちょう<rt>ちょう</rt>的<rt>てき</rt></ruby>にあらわす<ruby>記<rt>き</rt>号<rt>ごう</rt></ruby>であり、それ<ruby>自<rt>じ</rt>体<rt>たい</rt></ruby>に<ruby>固<rt>こ</rt>定<rt>てい</rt>的<rt>てき</rt></ruby>な<ruby>意<rt>い</rt>味<rt>み</rt></ruby>があるのではなく<ruby>人<rt>にん</rt>間<rt>げん</rt></ruby>が<ruby>意<rt>い</rt>味<rt>み</rt></ruby>をあてはめて<ruby>用<rt>もち</rt></ruby>いる<ruby>道<rt>どう</rt>具<rt>ぐ</rt></ruby>を<ruby>何<rt>なに</rt></ruby>と<ruby>呼<rt>よ</rt></ruby>ぶか、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "1. チャネル",
      "2. シンボル（<ruby>象<rt>しょう</rt>ちょう<rt>ちょう</rt></ruby>）",
      "3. フィードバック",
      "4. ノイズ（<ruby>雑<rt>ざつ</rt>音<rt>おん</rt></ruby>）"
    ],
    "answer": 2,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 2（シンボル（<ruby>象<rt>しょう</rt>ちょう<rt>ちょう</rt></ruby>））"
  },
  {
    "num": 15,
    "stem": "15. ホールの<ruby>対<rt>たい</rt>人<rt>じん</rt>距<rt>きょ</rt>離<rt>り</rt></ruby>の<ruby>分<rt>ぶん</rt>類<rt>るい</rt></ruby>において、<ruby>家<rt>か</rt>族<rt>ぞく</rt></ruby>や<ruby>恋<rt>こい</rt>人<rt>びと</rt></ruby>などごく<ruby>親<rt>した</rt></ruby>しい<ruby>間柄<rt>あいだがら</rt></ruby>で<ruby>用<rt>もち</rt></ruby>いられ、<ruby>当<rt>とう</rt>事<rt>じ</rt>者<rt>しゃ</rt>間<rt>かん</rt></ruby>でしか<ruby>聞<rt>き</rt></ruby>こえないひそひそ<ruby>声<rt>こえ</rt></ruby>で<ruby>話<rt>はな</rt></ruby>す<ruby>距<rt>きょ</rt>離<rt>り</rt></ruby>（0〜50cm）として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "1. <ruby>密<rt>みっ</rt>せつ<rt>せつ</rt>距<rt>きょ</rt>離<rt>り</rt></ruby>",
      "2. <ruby>個<rt>こ</rt>人<rt>じん</rt></ruby>の<ruby>距<rt>きょ</rt>離<rt>り</rt></ruby>（<ruby>個<rt>こ</rt>体<rt>たい</rt>的<rt>てき</rt>距<rt>きょ</rt>離<rt>り</rt></ruby>）",
      "3. <ruby>社<rt>しゃ</rt>会<rt>かい</rt>的<rt>てき</rt></ruby>な<ruby>距<rt>きょ</rt>離<rt>り</rt></ruby>",
      "4. <ruby>公<rt>こう</rt>的<rt>てき</rt></ruby>な<ruby>距<rt>きょ</rt>離<rt>り</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>密<rt>みっ</rt>せつ<rt>せつ</rt>距<rt>きょ</rt>離<rt>り</rt></ruby>）"
  },
  {
    "num": 16,
    "stem": "16. <ruby>非<rt>ひ</rt>言<rt>げん</rt>語<rt>ご</rt>的<rt>てき</rt></ruby>コミュニケーションのうち、OKサインやお<ruby>金<rt>かね</rt></ruby>の<ruby>合<rt>あい</rt>ず<rt>ず</rt></ruby>のように、<ruby>言<rt>げん</rt>語<rt>ご</rt></ruby>の<ruby>代<rt>か</rt></ruby>わりとなる<ruby>動<rt>どう</rt>作<rt>さ</rt></ruby>として<ruby>集<rt>しゅう</rt>団<rt>だん</rt>内<rt>ない</rt></ruby>で<ruby>広<rt>ひろ</rt></ruby>く<ruby>意<rt>い</rt>味<rt>み</rt></ruby>が<ruby>共<rt>きょう</rt>有<rt>ゆう</rt></ruby>されているものを<ruby>何<rt>なに</rt></ruby>と<ruby>呼<rt>よ</rt></ruby>ぶか、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "1. <ruby>例<rt>れい</rt>示<rt>じ</rt></ruby>（イラストレーション）",
      "2. <ruby>表<rt>ひょう</rt>象<rt>しょう</rt></ruby>（エンブレム）",
      "3. <ruby>適<rt>てき</rt>応<rt>おう</rt>動<rt>どう</rt>作<rt>さ</rt></ruby>（アダプター）",
      "4. <ruby>調<rt>ちょう</rt>整<rt>せい</rt>動<rt>どう</rt>作<rt>さ</rt></ruby>（レギュレーター）"
    ],
    "answer": 2,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 2（<ruby>表<rt>ひょう</rt>象<rt>しょう</rt></ruby>（エンブレム））"
  },
  {
    "num": 17,
    "section": "<ruby>第<rt>だい</rt></ruby>3<ruby>節<rt>せつ</rt></ruby> <ruby>対<rt>たい</rt>人<rt>じん</rt>援<rt>えん</rt>助<rt>じょ</rt>関<rt>かん</rt>係<rt>けい</rt></ruby>とコミュニケーション",
    "stem": "17. <ruby>対<rt>たい</rt>人<rt>じん</rt>援<rt>えん</rt>助<rt>じょ</rt></ruby>におけるコミュニケーションのスタイルとして、<ruby>自<rt>じ</rt>分<rt>ぶん</rt></ruby>の<ruby>意<rt>い</rt>見<rt>けん</rt></ruby>や<ruby>要<rt>よう</rt>望<rt>ぼう</rt></ruby>を<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>に<ruby>伝<rt>つた</rt></ruby>えると<ruby>同<rt>どう</rt>時<rt>じ</rt></ruby>に、<ruby>相<rt>あい</rt>手<rt>て</rt></ruby>の<ruby>思<rt>おも</rt></ruby>いも<ruby>大<rt>たい</rt>切<rt>せつ</rt></ruby>にして<ruby>相<rt>そう</rt>互<rt>ご</rt>尊<rt>そん</rt>重<rt>ちょう</rt></ruby>を<ruby>目<rt>め</rt>ざ<rt>ざ</rt></ruby>す<ruby>姿<rt>し</rt>勢<rt>せい</rt></ruby>として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "1. ノンアサーティブ・コミュニケーション",
      "2. アグレッシブ・コミュニケーション",
      "3. アサーティブ・コミュニケーション",
      "4. パターナリスティック・コミュニケーション"
    ],
    "answer": 3,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 3（アサーティブ・コミュニケーション）"
  },
  {
    "num": 18,
    "stem": "18. <ruby>対<rt>たい</rt>人<rt>じん</rt>援<rt>えん</rt>助<rt>じょ</rt></ruby>における<ruby>基<rt>き</rt>本<rt>ほん</rt>姿<rt>し</rt>勢<rt>せい</rt></ruby>である「<ruby>受<rt>じゅ</rt>用<rt>よう</rt></ruby>」の<ruby>せつ<rt>せつ</rt>めい<rt>めい</rt></ruby>として、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "1. <ruby>利<rt>り</rt>用<rt>よう</rt>者<rt>しゃ</rt></ruby>のどのような<ruby>行<rt>こう</rt>動<rt>どう</rt></ruby>や<ruby>違<rt>い</rt>法<rt>ほう</rt></ruby>な<ruby>行<rt>こう</rt>為<rt>い</rt></ruby>もすべて<ruby>正<rt>ただ</rt></ruby>しいと<ruby>認<rt>みと</rt></ruby>めること",
      "2. <ruby>援<rt>えん</rt>助<rt>じょ</rt>者<rt>しゃ</rt></ruby>の<ruby>個<rt>こ</rt>人<rt>じん</rt>的<rt>てき</rt></ruby>な<ruby>価<rt>か</rt>値<rt>ち</rt>観<rt>かん</rt></ruby>に<ruby>照<rt>て</rt></ruby>らして<ruby>利<rt>り</rt>用<rt>よう</rt>者<rt>しゃ</rt></ruby>の<ruby>善<rt>ぜん</rt>悪<rt>あく</rt></ruby>を<ruby>指<rt>し</rt>導<rt>どう</rt></ruby>すること",
      "3. <ruby>利<rt>り</rt>用<rt>よう</rt>者<rt>しゃ</rt></ruby>の<ruby>言<rt>げん</rt>動<rt>どう</rt></ruby>を<ruby>援<rt>えん</rt>助<rt>じょ</rt>者<rt>しゃ</rt></ruby>の<ruby>価<rt>か</rt>値<rt>ち</rt>基<rt>き</rt>準<rt>じゅん</rt></ruby>で<ruby>判<rt>はん</rt>断<rt>だん</rt></ruby>せず、1<ruby>人<rt>ひと</rt></ruby>の<ruby>価<rt>か</rt>値<rt>ち</rt></ruby>ある<ruby>人<rt>にん</rt>間<rt>げん</rt></ruby>としてありのまま<ruby>受<rt>う</rt></ruby>け<ruby>入<rt>い</rt></ruby>れること",
      "4. <ruby>利<rt>り</rt>用<rt>よう</rt>者<rt>しゃ</rt></ruby>の<ruby>抱<rt>かか</rt></ruby>える<ruby>課<rt>か</rt>題<rt>だい</rt></ruby>を<ruby>援<rt>えん</rt>助<rt>じょ</rt>者<rt>しゃ</rt></ruby>がすべて<ruby>肩<rt>かた</rt>代<rt>が</rt></ruby>わりして<ruby>解<rt>かい</rt>決<rt>けつ</rt></ruby>すること"
    ],
    "answer": 3,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 3（<ruby>利<rt>り</rt>用<rt>よう</rt>者<rt>しゃ</rt></ruby>の<ruby>言<rt>げん</rt>動<rt>どう</rt></ruby>を<ruby>援<rt>えん</rt>助<rt>じょ</rt>者<rt>しゃ</rt></ruby>の<ruby>価<rt>か</rt>値<rt>ち</rt>基<rt>き</rt>準<rt>じゅん</rt></ruby>で<ruby>判<rt>はん</rt>断<rt>だん</rt></ruby>せず、1<ruby>人<rt>ひと</rt></ruby>の<ruby>価<rt>か</rt>値<rt>ち</rt></ruby>ある<ruby>人<rt>にん</rt>間<rt>げん</rt></ruby>としてありのまま<ruby>受<rt>う</rt></ruby>け<ruby>入<rt>い</rt></ruby>れること）"
  },
  {
    "num": 19,
    "stem": "19. <ruby>対<rt>たい</rt>人<rt>じん</rt>援<rt>えん</rt>助<rt>じょ</rt></ruby>における「<ruby>共<rt>きょう</rt>感<rt>かん</rt></ruby>」と「<ruby>同<rt>どう</rt>情<rt>じょう</rt></ruby>」の<ruby>違<rt>ちが</rt></ruby>いについて、<ruby>最<rt>もっと</rt></ruby>も<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "1. <ruby>同<rt>どう</rt>情<rt>じょう</rt></ruby>は<ruby>相<rt>あい</rt>手<rt>て</rt></ruby>の<ruby>立<rt>たち</rt>場<rt>ば</rt></ruby>に<ruby>立<rt>た</rt></ruby>ち、<ruby>共<rt>きょう</rt>感<rt>かん</rt></ruby>は<ruby>自<rt>じ</rt>分<rt>ぶん</rt>自<rt>じ</rt>身<rt>しん</rt></ruby>の<ruby>感<rt>かん</rt>情<rt>じょう</rt></ruby>を<ruby>基<rt>き</rt>準<rt>じゅん</rt></ruby>にして<ruby>哀<rt>あわ</rt></ruby>れむこと",
      "2. <ruby>同<rt>どう</rt>情<rt>じょう</rt></ruby>は<ruby>自<rt>じ</rt>分<rt>ぶん</rt></ruby>を<ruby>基<rt>き</rt>準<rt>じゅん</rt></ruby>にして<ruby>相<rt>あい</rt>手<rt>て</rt></ruby>の<ruby>感<rt>かん</rt>情<rt>じょう</rt></ruby>を<ruby>理<rt>り</rt>解<rt>かい</rt></ruby>しようとし、<ruby>共<rt>きょう</rt>感<rt>かん</rt></ruby>は<ruby>相<rt>あい</rt>手<rt>て</rt></ruby>を<ruby>基<rt>き</rt>準<rt>じゅん</rt></ruby>にして<ruby>相<rt>あい</rt>手<rt>て</rt></ruby>の<ruby>立<rt>たち</rt>場<rt>ば</rt></ruby>から<ruby>感<rt>かん</rt>情<rt>じょう</rt></ruby>を<ruby>理<rt>り</rt>解<rt>かい</rt></ruby>しようとすること",
      "3. <ruby>援<rt>えん</rt>助<rt>じょ</rt>関<rt>かん</rt>係<rt>けい</rt></ruby>においては<ruby>同<rt>どう</rt>情<rt>じょう</rt></ruby>が<ruby>最<rt>もっと</rt></ruby>も<ruby>重<rt>じゅう</rt>視<rt>し</rt></ruby>され、<ruby>共<rt>きょう</rt>感<rt>かん</rt></ruby>は<ruby>避<rt>さ</rt></ruby>けるべき<ruby>感<rt>かん</rt>情<rt>じょう</rt></ruby>である",
      "4. <ruby>共<rt>きょう</rt>感<rt>かん</rt></ruby>と<ruby>同<rt>どう</rt>情<rt>じょう</rt></ruby>は<ruby>心<rt>しん</rt>理<rt>り</rt>学<rt>がく</rt>上<rt>じょう</rt></ruby>まったく<ruby>同<rt>どう</rt>一<rt>いつ</rt></ruby>の<ruby>意<rt>い</rt>味<rt>み</rt></ruby>であり<ruby>区<rt>く</rt>別<rt>べつ</rt></ruby>されない"
    ],
    "answer": 2,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 2（<ruby>同<rt>どう</rt>情<rt>じょう</rt></ruby>は<ruby>自<rt>じ</rt>分<rt>ぶん</rt></ruby>を<ruby>基<rt>き</rt>準<rt>じゅん</rt></ruby>にして<ruby>相<rt>あい</rt>手<rt>て</rt></ruby>の<ruby>感<rt>かん</rt>情<rt>じょう</rt></ruby>を<ruby>理<rt>り</rt>解<rt>かい</rt></ruby>しようとし、<ruby>共<rt>きょう</rt>感<rt>かん</rt></ruby>は<ruby>相<rt>あい</rt>手<rt>て</rt></ruby>を<ruby>基<rt>き</rt>準<rt>じゅん</rt></ruby>にして<ruby>相<rt>あい</rt>手<rt>て</rt></ruby>の<ruby>立<rt>たち</rt>場<rt>ば</rt></ruby>から<ruby>感<rt>かん</rt>情<rt>じょう</rt></ruby>を<ruby>理<rt>り</rt>解<rt>かい</rt></ruby>しようとすること）"
  },
  {
    "num": 20,
    "stem": "20. バイステックの7<ruby>原<rt>げん</rt>則<rt>そく</rt></ruby>において、「<ruby>利<rt>り</rt>用<rt>よう</rt>者<rt>しゃ</rt></ruby>が<ruby>抱<rt>かか</rt></ruby>くさまざまな<ruby>感<rt>かん</rt>情<rt>じょう</rt></ruby>（<ruby>特<rt>とく</rt></ruby>に<ruby>否<rt>ひ</rt>定<rt>てい</rt>的<rt>てき</rt>感<rt>かん</rt>情<rt>じょう</rt></ruby>）を<ruby>自<rt>じ</rt>由<rt>ゆう</rt></ruby>に<ruby>表<rt>ひょう</rt>現<rt>げん</rt></ruby>することを<ruby>認<rt>みと</rt></ruby>め、<ruby>意<rt>い</rt>と<rt>と</rt>的<rt>てき</rt></ruby>に<ruby>表<rt>ひょう</rt>出<rt>しゅつ</rt></ruby>を<ruby>促<rt>うなが</rt></ruby>す」<ruby>原<rt>げん</rt>則<rt>そく</rt></ruby>として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "1. <ruby>個<rt>こ</rt>べつ<rt>べつ</rt>か<rt>か</rt></ruby>の<ruby>原<rt>げん</rt>則<rt>そく</rt></ruby>",
      "2. <ruby>意<rt>い</rt>と<rt>と</rt>的<rt>てき</rt></ruby>な<ruby>感<rt>かん</rt>情<rt>じょう</rt></ruby>の<ruby>表<rt>ひょう</rt>出<rt>しゅつ</rt></ruby>の<ruby>原<rt>げん</rt>則<rt>そく</rt></ruby>",
      "3. <ruby>統<rt>とう</rt>制<rt>せい</rt></ruby>された<ruby>情<rt>じょう</rt>緒<rt>ちょ</rt>的<rt>てき</rt>関<rt>かん</rt>与<rt>よ</rt></ruby>の<ruby>原<rt>げん</rt>則<rt>そく</rt></ruby>",
      "4. <ruby>非<rt>ひ</rt>審<rt>しん</rt>判<rt>ぱん</rt>的<rt>てき</rt>態<rt>たい</rt>度<rt>ど</rt></ruby>の<ruby>原<rt>げん</rt>則<rt>そく</rt></ruby>"
    ],
    "answer": 2,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 2（<ruby>意<rt>い</rt>と<rt>と</rt>的<rt>てき</rt></ruby>な<ruby>感<rt>かん</rt>情<rt>じょう</rt></ruby>の<ruby>表<rt>ひょう</rt>出<rt>しゅつ</rt></ruby>の<ruby>原<rt>げん</rt>則<rt>そく</rt></ruby>）"
  },
  {
    "num": 21,
    "stem": "21. バイステックの7<ruby>原<rt>げん</rt>則<rt>そく</rt></ruby>において、「<ruby>援<rt>えん</rt>助<rt>じょ</rt>者<rt>しゃ</rt></ruby>がみずからの<ruby>価<rt>か</rt>値<rt>ち</rt>観<rt>かん</rt></ruby>や<ruby>道<rt>どう</rt>徳<rt>とく</rt>的<rt>てき</rt>基<rt>き</rt>準<rt>じゅん</rt></ruby>によって、<ruby>利<rt>り</rt>用<rt>よう</rt>者<rt>しゃ</rt></ruby>の<ruby>考<rt>かんが</rt></ruby>えや<ruby>過<rt>か</rt>こ<rt>こ</rt></ruby>の<ruby>行<rt>こう</rt>動<rt>どう</rt></ruby>を<ruby>いっ<rt>いっ</rt>ぽう<rt>ぽう</rt>てき<rt>てき</rt></ruby>に<ruby>批<rt>ひ</rt>判<rt>はん</rt></ruby>・<ruby>非<rt>ひ</rt>難<rt>なん</rt></ruby>してはならない」とする<ruby>原<rt>げん</rt>則<rt>そく</rt></ruby>として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "1. <ruby>受<rt>じゅ</rt>用<rt>よう</rt></ruby>の<ruby>原<rt>げん</rt>則<rt>そく</rt></ruby>",
      "2. <ruby>非<rt>ひ</rt>審<rt>しん</rt>判<rt>ぱん</rt>的<rt>てき</rt>態<rt>たい</rt>度<rt>ど</rt></ruby>の<ruby>原<rt>げん</rt>則<rt>そく</rt></ruby>",
      "3. <ruby>自<rt>じ</rt>己<rt>こ</rt>決<rt>けっ</rt>定<rt>てい</rt></ruby>の<ruby>原<rt>げん</rt>則<rt>そく</rt></ruby>",
      "4. <ruby>秘<rt>ひ</rt>密<rt>みつ</rt>保<rt>ほ</rt>持<rt>じ</rt></ruby>の<ruby>原<rt>げん</rt>則<rt>そく</rt></ruby>"
    ],
    "answer": 2,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 2（<ruby>非<rt>ひ</rt>審<rt>しん</rt>判<rt>ぱん</rt>的<rt>てき</rt>態<rt>たい</rt>度<rt>ど</rt></ruby>の<ruby>原<rt>げん</rt>則<rt>そく</rt></ruby>）"
  },
  {
    "num": 22,
    "section": "<ruby>第<rt>だい</rt></ruby>4<ruby>節<rt>せつ</rt></ruby> <ruby>組<rt>そ</rt>織<rt>しき</rt></ruby>におけるコミュニケーション",
    "stem": "22. <ruby>組<rt>そ</rt>織<rt>しき</rt></ruby>におけるタテの<ruby>情<rt>じょう</rt>報<rt>ほう</rt></ruby>の<ruby>流<rt>なが</rt></ruby>れのうち、<ruby>現<rt>げん</rt>場<rt>ば</rt></ruby>のスタッフが<ruby>気<rt>き</rt></ruby>づいた<ruby>日<rt>にち</rt>常<rt>じょう</rt></ruby>の<ruby>変<rt>へん</rt>化<rt>か</rt></ruby>や<ruby>業<rt>ぎょう</rt>務<rt>む</rt>上<rt>じょう</rt></ruby>の<ruby>課<rt>か</rt>題<rt>だい</rt></ruby>、<ruby>改<rt>かい</rt>善<rt>ぜん</rt>提<rt>てい</rt>案<rt>あん</rt></ruby>などを<ruby>上<rt>じょう</rt>層<rt>そう</rt>部<rt>ぶ</rt></ruby>へと<ruby>伝<rt>でん</rt>達<rt>たつ</rt></ruby>する<ruby>意<rt>い</rt>し<rt>し</rt>そ<rt>そ</rt>つう<rt>つう</rt></ruby>（<ruby>か<rt>か</rt>い<rt>い</rt>じょう<rt>じょう</rt>たつ<rt>たつ</rt></ruby>）として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "1. トップダウンのコミュニケーション",
      "2. ボトムアップのコミュニケーション",
      "3. <ruby>水<rt>すい</rt>平<rt>へい</rt>的<rt>てき</rt></ruby>なコミュニケーション",
      "4. インフォーマルなコミュニケーション"
    ],
    "answer": 2,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 2（ボトムアップのコミュニケーション）"
  },
  {
    "num": 23,
    "stem": "23. <ruby>集<rt>しゅう</rt>団<rt>だん</rt></ruby>で<ruby>討<rt>とう</rt>論<rt>ろん</rt></ruby>や<ruby>意<rt>い</rt>し<rt>し</rt>けっ<rt>けっ</rt>てい<rt>てい</rt></ruby>を<ruby>行<rt>おこな</rt></ruby>う<ruby>際<rt>さい</rt></ruby>、<ruby>多<rt>た</rt>様<rt>よう</rt></ruby>な<ruby>意<rt>い</rt>見<rt>けん</rt></ruby>を<ruby>じゅう<rt>じゅう</rt>ぶん<rt>ぶん</rt></ruby>に<ruby>評<rt>ひょう</rt>価<rt>か</rt></ruby>することなく、<ruby>集<rt>しゅう</rt>団<rt>だん</rt></ruby>としての<ruby>意<rt>い</rt>見<rt>けん</rt></ruby>の<ruby>いっ<rt>いっ</rt>ち<rt>ち</rt></ruby>や<ruby>けっ<rt>けっ</rt>そく<rt>そく</rt></ruby>を<ruby>優<rt>ゆう</rt>先<rt>せん</rt></ruby>させて<ruby>安<rt>あん</rt>ちょく<rt>ちょく</rt></ruby>な<ruby>合<rt>ごう</rt>い<rt>い</rt></ruby>に<ruby>至<rt>いた</rt></ruby>ってしまう<ruby>現<rt>げん</rt>象<rt>しょう</rt></ruby>として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "1. <ruby>集<rt>しゅう</rt>団<rt>だん</rt>浅<rt>せん</rt>慮<rt>りょ</rt></ruby>（グループシンク）",
      "2. <ruby>集<rt>しゅう</rt>団<rt>だん</rt>極<rt>きょく</rt>性<rt>せい</rt>化<rt>か</rt></ruby>（<ruby>集<rt>しゅう</rt>団<rt>だん</rt>分<rt>ぶん</rt>極<rt>きょく</rt>化<rt>か</rt></ruby>）",
      "3. コーシャスシフト",
      "4. ブーメラン<ruby>効<rt>こう</rt>果<rt>か</rt></ruby>"
    ],
    "answer": 1,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 1（<ruby>集<rt>しゅう</rt>団<rt>だん</rt>浅<rt>せん</rt>慮<rt>りょ</rt></ruby>（グループシンク））"
  },
  {
    "num": 24,
    "stem": "24. <ruby>自<rt>じ</rt>由<rt>ゆう</rt></ruby>なアイデアを<ruby>開<rt>かい</rt>発<rt>はつ</rt></ruby>するためのブレーンストーミング（BS）の4<ruby>原<rt>げん</rt>則<rt>そく</rt></ruby>に<ruby>含<rt>ふく</rt></ruby>まれないものとして、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "1. <ruby>批<rt>ひ</rt>判<rt>はん</rt>厳<rt>げん</rt>禁<rt>きん</rt></ruby>（その<ruby>場<rt>ば</rt></ruby>ですぐに<ruby>善<rt>ぜん</rt>悪<rt>あく</rt></ruby>の<ruby>判<rt>はん</rt>断<rt>だん</rt></ruby>や<ruby>批<rt>ひ</rt>判<rt>はん</rt></ruby>をしない）",
      "2. <ruby>自<rt>じ</rt>由<rt>ゆう</rt>奔<rt>ほん</rt>放<rt>ぽう</rt></ruby>（<ruby>き<rt>き</rt>ばつ<rt>ばつ</rt></ruby>なアイデアを<ruby>かん<rt>かん</rt>げい<rt>げい</rt></ruby>し<ruby>自<rt>じ</rt>由<rt>ゆう</rt></ruby>に<ruby>はっ<rt>はっ</rt>そう<rt>そう</rt></ruby>する）",
      "3. <ruby>品<rt>ひん</rt>質<rt>しつ</rt>優<rt>ゆう</rt>先<rt>せん</rt></ruby>（アイデアの<ruby>量<rt>りょう</rt></ruby>よりも<ruby>さい<rt>さい</rt>しょ<rt>しょ</rt></ruby>から<ruby>かん<rt>かん</rt>せい<rt>せい</rt>ど<rt>ど</rt></ruby>の<ruby>高<rt>たか</rt></ruby>い<ruby>質<rt>しつ</rt></ruby>を<ruby>求<rt>もと</rt></ruby>める）",
      "4. <ruby>便<rt>びん</rt>じょう<rt>じょう</rt>発<rt>はっ</rt>展<rt>てん</rt></ruby>（<ruby>た<rt>た</rt>にん<rt>にん</rt></ruby>のアイデアを<ruby>さん<rt>さん</rt>こう<rt>こう</rt></ruby>にして<ruby>れん<rt>れん</rt>そう<rt>そう</rt></ruby>・<ruby>かい<rt>かい</rt>ぜん<rt>ぜん</rt></ruby>する）"
    ],
    "answer": 3,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 3（<ruby>品<rt>ひん</rt>質<rt>しつ</rt>優<rt>ゆう</rt>先<rt>せん</rt></ruby>（アイデアの<ruby>量<rt>りょう</rt></ruby>よりも<ruby>さい<rt>さい</rt>しょ<rt>しょ</rt></ruby>から<ruby>かん<rt>かん</rt>せい<rt>せい</rt>ど<rt>ど</rt></ruby>の<ruby>高<rt>たか</rt></ruby>い<ruby>質<rt>しつ</rt></ruby>を<ruby>求<rt>もと</rt></ruby>める）※<ruby>正<rt>ただ</rt></ruby>しくは「<ruby>多<rt>た</rt>量<rt>りょう</rt>提<rt>てい</rt>案<rt>あん</rt></ruby>」）"
  },
  {
    "num": 25,
    "stem": "25. <ruby>職<rt>しょく</rt>ば<rt>ば</rt></ruby>における<ruby>人<rt>じん</rt>材<rt>ざい</rt>育<rt>いく</rt>成<rt>せい</rt>手<rt>しゅ</rt>法<rt>ほう</rt></ruby>のうち、<ruby>指<rt>し</rt>じ<rt>じ</rt></ruby>や<ruby>答<rt>こた</rt></ruby>えを<ruby>いっ<rt>いっ</rt>ぽう<rt>ぽう</rt>てき<rt>てき</rt></ruby>に<ruby>教<rt>おし</rt></ruby>えるのではなく、<ruby>質<rt>しつ</rt>問<rt>もん</rt></ruby>を<ruby>投<rt>な</rt></ruby>げかけることで<ruby>相<rt>あい</rt>手<rt>て</rt>自<rt>じ</rt>身<rt>しん</rt></ruby>に<ruby>考<rt>かんが</rt></ruby>えさせ、<ruby>答<rt>こた</rt></ruby>えを<ruby>引<rt>ひ</rt></ruby>き<ruby>出<rt>だ</rt></ruby>していくアプローチとして、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
    "options": [
      "1. ティーチング",
      "2. コーチング",
      "3. メンタリング",
      "4. モデリング"
    ],
    "answer": 2,
    "exp": "<ruby>選<rt>せん</rt>択<rt>たく</rt>肢<rt>し</rt></ruby> 2（コーチング）"
  }
]

# 回答入力フォーム
user_answers = {}

st.markdown("---")
st.markdown("### ✍️ 練習問題（各問の選択肢を選んでください）")

for q in questions:
    if "chapter" in q:
        st.markdown(f"<div class='chapter-header'>{q['chapter']}</div>", unsafe_allow_html=True)
    if "section" in q:
        st.markdown(f"<div class='section-header'>{q['section']}</div>", unsafe_allow_html=True)

    st.markdown(f"<div class='q-title'>{q['stem']}</div>", unsafe_allow_html=True)
    
    for opt in q['options']:
        st.markdown(f"<div class='opt-item'>{opt}</div>", unsafe_allow_html=True)
    
    selected_idx = st.radio(
        label=f"Q{q['num']}の回答を選択:",
        options=[1, 2, 3, 4],
        index=None,
        horizontal=True,
        key=f"q_{q['num']}"
    )
    user_answers[q['num']] = selected_idx
    st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)

# 採点・提出ファイル作成ボタン
st.markdown("---")
if st.button("📊 採点して提出用レポートを作成する", type="primary", use_container_width=True):
    if not s_class.strip() or not s_id.strip() or not s_name.strip():
        st.error("⚠️ 「組（クラス名）」「学籍番号」「氏名」をすべて入力してください。")
    else:
        score = 0
        unanswered = 0
        report_rows = ""
        
        for q in questions:
            u_ans = user_answers[q['num']]
            is_correct = (u_ans == q['answer'])
            if u_ans is None:
                unanswered += 1
                status = "<span style='color:red;'>未回答 ×</span>"
            elif is_correct:
                score += 1
                status = "<span style='color:green;'>正解 ○</span>"
            else:
                status = "<span style='color:red;'>不正解 ×</span>"
            
            report_rows += f"""
            <tr>
              <td style='padding:6px;border:1px solid #ccc;text-align:center;'>第 {q['num']} 問</td>
              <td style='padding:6px;border:1px solid #ccc;text-align:center;'>{u_ans if u_ans else '未回答'}</td>
              <td style='padding:6px;border:1px solid #ccc;text-align:center;'>{q['answer']}</td>
              <td style='padding:6px;border:1px solid #ccc;text-align:center;'>{status}</td>
            </tr>
            """
        
        total = len(questions)
        percent = round((score / total) * 100)
        
        st.success(f"🎉 採点が完了しました！ 得点: **{score} / {total} 点**（正答率: {percent}%）")
        if unanswered > 0:
            st.warning(f"※ 未回答の問題が {unanswered} 問ありました。")

        timestamp = datetime.datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")
        auth_raw = f"{s_class}_{s_id}_{s_name}_{score}_{timestamp}"
        auth_code = f"VER2-{abs(hash(auth_raw)):X}-{datetime.datetime.now().strftime('%f')}"

        report_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>提出用レポート_{html.escape(s_name)}</title>
<style>
  body {{ font-family: "Hiragino Mincho ProN", "Yu Mincho", serif; padding: 25px; line-height: 1.6; color: #222; }}
  .report-box {{ max-width: 650px; margin: 0 auto; border: 2px solid #1e3a8a; padding: 20px; border-radius: 6px; }}
  h2 {{ text-align: center; border-bottom: 2px solid #1e3a8a; padding-bottom: 8px; margin-top: 0; color: #1e3a8a; }}
  .info-table {{ width: 100%; border-collapse: collapse; margin-bottom: 16px; }}
  .info-table td {{ padding: 6px 10px; border: 1px solid #999; }}
  .info-table td.header {{ background: #eee; font-weight: bold; width: 30%; }}
  .score-box {{ text-align: center; background: #eff6ff; border: 1px solid #3b82f6; padding: 12px; margin-bottom: 16px; border-radius: 4px; }}
  .score-box span {{ font-size: 1.8rem; font-weight: bold; color: #1e3a8a; }}
  table.results {{ width: 100%; border-collapse: collapse; font-size: 0.9rem; }}
  table.results th {{ background: #f1f5f9; padding: 6px; border: 1px solid #ccc; }}
  .auth-tag {{ font-family: monospace; font-size: 0.8rem; color: #64748b; word-break: break-all; margin-top: 15px; border-top: 1px dashed #ccc; padding-top: 8px; }}
</style>
</head>
<body>
<div class="report-box">
  <h2>課題提出用 成績レポート</h2>
  <table class="info-table">
    <tr><td class="header">教科・課題</td><td>No.2 人間関係とコミュニケーション 練習問題（4択）</td></tr>
    <tr><td class="header">組（クラス）</td><td>{html.escape(s_class)}</td></tr>
    <tr><td class="header">学籍番号</td><td>{html.escape(s_id)}</td></tr>
    <tr><td class="header">氏名</td><td>{html.escape(s_name)}</td></tr>
    <tr><td class="header">実施日時</td><td>{timestamp}</td></tr>
  </table>
  <div class="score-box">
    得点：<span>{score} / {total} 点</span>（正答率 {percent}%）
  </div>
  <h3>各設問の回答記録</h3>
  <table class="results">
    <thead>
      <tr><th>設問番号</th><th>あなたの回答</th><th>正解</th><th>判定</th></tr>
    </thead>
    <tbody>
      {report_rows}
    </tbody>
  </table>
  <div class="auth-tag">
    【改ざん防止用 認証コード】<br>{auth_code}
  </div>
</div>
</body>
</html>"""

        st.markdown("### 📥 課題提出手順")
        st.info("""
        1. 下の **「提出用レポート（HTML）を保存」** ボタンを押して、成績レポートファイルを保存してください。
        2. Google Classroom の該当課題ページを開きます。
        3. **「あなたの課題」→「追加または作成」→「ファイル」** からダウンロードしたファイルを添付し、**「提出」** を押してください。
        """)

        file_name = f"提出用_人間の理解_{s_id}_{s_name}.html"
        st.download_button(
            label="📥 提出用レポート（HTML）を保存",
            data=report_html,
            file_name=file_name,
            mime="text/html",
            use_container_width=True
        )

        st.markdown("[Google Classroom を開く ↗]([suspicious link removed])", unsafe_allow_html=True)
