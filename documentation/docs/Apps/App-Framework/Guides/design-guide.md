# App Developer Design Guide

Domo adheres to Material Design principles, and we highly encourage that you consider these same principles when building a Domo app as they will ensure a seamless transition from Domo to your app.

Please be familiar with the following principles and guidelines as you design your app:

<ul>
 	<li><a href="https://material.io/guidelines/">Material Design Guidelines</a></li>
 	<li><a href="https://developer.apple.com/design/">App iOS Design Principles</a></li>
</ul>

### Domo Color Palette

---

You're welcome to use the color palette of your choice when designing your app; however, designers will often want to design the app to look and feel more like native Domo. If that's the route you want to take, we've provided the basic Domo color palette for your reference.

#### Domo Blue Palette

<div class="color-palette">
    <span style="background: #ffffff;">#ffffff</span>
    <span style="background: #f2f8fc;">#f2f8fc</span>
    <span style="background: #dcedf8;">#dcedf8</span>
    <span style="background: #c8e2f4;">#c8e2f4</span>
    <span style="background: #b2d7f0;">#b2d7f0</span>
    <span style="background: #99ccee;">#99ccee</span>
</div>

#### Gray Palette

<div class="color-palette">
    <span style="background: #f6f6f6;">#f6f6f6</span>
    <span style="background: #eeeeee;">#eeeeee</span>
    <span style="background: #d4d4d4;">#d4d4d4</span>
    <span style="background: #888888;">#888888</span>
    <span style="background: #555555;">#555555</span>
    <span style="background: #333333;">#333333</span>
</div>

#### Button Palette

<div class="color-palette -headers">
    <span>Border</span>
    <span>Background</span>
    <span>Background:Hover</span>
    <span>Background:Active</span>
</div>

<div class="color-palette">
    <span style="background: #ccc; color: rgba(0, 0, 0, .6);">#cccccc</span>
    <span style="background: #rgba(255,255,255,.5); color: rgba(0, 0, 0, .6);">rgba(255,255,255,0.5)</span>
    <span style="background: #F8F8F8; color: rgba(0, 0, 0, .6);">#f8f8f8</span>
    <span style="background: #E6E6E6; color: rgba(0, 0, 0, .6);">#e6e6e6</span>
</div>

<div class="color-palette">
    <span style="background: #fc9927; color: white;">#fc9927</span>
    <span style="background: #fc8f13; color: white;">#fc8f13</span>
    <span style="background: #fc8f13; color: white;">#fc8f13</span>
    <span style="background: #ed8003; color: white;">#ed8003</span>
</div>

<div class="color-palette">
    <span style="background: #cb2c1c; color: white;">#cb2c1c</span>
    <span style="background: #cb2c1c; color: white;">#cb2c1c</span>
    <span style="background: #b9281a; color: white;">#b9281a</span>
    <span style="background: #9e2216; color: white;">#9e2216</span>
</div>

#### Link Palette

<div class="color-palette">
    <span style="background: #4b87b0; color: #fff;">#4b87b0: Default</span>
    <span style="background: #43799e; color: #fff;">#43799e: Hover</span>
</div>

#### Chart Palette

##### Colors

<div class="chart-container">
<div class="color-palette -chart">
    <span style="background: #d9ebfd;">#d9ebfd</span>
    <span style="background: #b7daf5;">#b7daf5</span>
    <span style="background: #90c4e4;">#90c4e4</span>
    <span style="background: #72b0d7;">#72b0d7</span>
    <span style="background: #4e8cba;">#4e8cba</span>
    <span style="background: #31689b;">#31689b</span>
</div>
<div class="color-palette -chart">
    <span style="background:#ddf4ba;">#ddf4ba</span>
    <span style="background:#bbe491;">#bbe491</span>
    <span style="background:#a0d771;">#a0d771</span>
    <span style="background:#80c25d;">#80c25d</span>
    <span style="background:#559e38;">#559e38</span>
    <span style="background:#347b26;">#347b26</span>
</div>
<div class="color-palette -chart">
    <span style="background:#fdecad;">#fdecad</span>
    <span style="background:#fccf84;">#fccf84</span>
    <span style="background:#fbad56;">#fbad56</span>
    <span style="background:#fb8d34;">#fb8d34</span>
    <span style="background:#e45621;">#e45621</span>
    <span style="background:#a43724;">#a43724</span>
</div>

<div class="color-palette -chart">
    <span style="background:#f3e4fe;">#f3e4fe</span>
    <span style="background:#ddc8ef;">#ddc8ef</span>
    <span style="background:#c5acde;">#c5acde</span>
    <span style="background:#b391ca;">#b391ca</span>
    <span style="background:#8f6cc0;">#8f6dc0</span>
    <span style="background:#7940a1;">#7940a1</span>
</div>
<div class="color-palette -chart">
    <span style="background:#d8f4de;">#d8f4de</span>
    <span style="background:#8be4ca;">#8be4ca</span>
    <span style="background:#8dd5be;">#8dd5be</span>
    <span style="background:#69bea8;">#69bea8</span>
    <span style="background:#46998a;">#46998a</span>
    <span style="background:#227872;">#227872</span>
</div>
<div class="color-palette -chart">
    <span style="background:#fcd7e6;">#fcd7e6</span>
    <span style="background:#fbb6dd;">#fbb6dd</span>
    <span style="background:#f395cd;">#f395cd</span>
    <span style="background:#ee76bf;">#ee76bf</span>
    <span style="background:#cf51ac;">#cf51ac</span>
    <span style="background:#a62a92;">#a62a92</span>
</div>
<div class="color-palette -chart">
    <span style="background:#fddddd;">#fddddd</span>
    <span style="background:#fcbcb7;">#fcbcb7</span>
    <span style="background:#fd9a93;">#fd9a93</span>
    <span style="background:#fd7f76;">#fd7f76</span>
    <span style="background:#e45850;">#e45850</span>
    <span style="background:#c92e25;">#c92e25</span>
</div>
</div>

#### Rules

When coloring multi-series charts, be sure to alternate the color saturation. Choosing colors with the same saturation will eliminate contrasts, creating unnecessary eye strain.

**Bad Example**

<div class="color-palette">
    <span style="background:#b7daf5">#b7daf5</span>
    <span style="background:#bbe491">#bbe491</span>
    <span style="background:#fccf84">#fccf84</span>
    <span style="background:#ddc8ef">#ddc8ef</span>
    <span style="background:#abe4ca">#abe4ca</span>
    <span style="background:#fbb6dd">#fbb6dd</span>
</div>

**Good Example**

<div class="color-palette">
    <span style="background:#90c4e4;">#90c4e4</span>
    <span style="background:#4e8cba;">#4e8cba</span>
    <span style="background:#a0d771;">#a0d771</span>
    <span style="background:#559e38;">#559e38</span>
    <span style="background:#fbad56;">#fbad56</span>
    <span style="background:#e45621;">#e45621</span>
</div>

### Typography

---

Domo’s typography foundation lies in traditional typographical measures, utilizing a 6px baseline grid. All pages are designed using spacing units of 6 between different components. This creates a pleasing and predictable vertical rhythm and extends to our horizontal grid as well.

Again, you're not required to use Domo styling in your app, but many designers have requested these guides in order to design their app to look and feel more like Domo.

<div class="typography-category">Jumbo</div>
<div class="typography-label">Size/Leading: 64/72 • Weight: Light 300</div>
<div style="color:rgba(0,0,0,1); font-size:64px; line-height:72px; font-weight:300;">The quick, brown fox</div>

<div class="typography-category">Display-1</div>
<div class="typography-label">Size/Leading: 36/48 • Weight: Light 300 • 80% Black</div>
<div style="color:rgba(0,0,0,.8); font-size:36px; line-height: 48px; font-weight:300;">The quick, brown fox</div>

<div class="typography-category">Display-2</div>
<div class="typography-label">Size/Leading: 30/42 • Weight: Light 300 • 80% Black</div>
<div style="color:rgba(0,0,0,.8); font-size:30px; line-height:42px; font-weight:300;">The quick, brown fox</div>

<div class="typography-category">Display-3</div>
<div class="typography-label">Size/Leading: 24/32 • Weight: Light 300 • 80% Black</div>
<div style="color:rgba(0,0,0,.8); font-size:24px; line-height:32px; font-weight:300;">The quick, brown fox</div>

<div class="typography-category">Display-4</div>
<div class="typography-label">Size/Leading: 20/28 • Weight: Regular 400 • 80% Black</div>
<div style="color:rgba(0,0,0,.8); font-size:20px; line-height:28px; font-weight:400;">The quick, brown fox</div>

<div class="typography-category">Display-5</div>
<div class="typography-label">Size/Leading: 18/24 • Weight: Regular 400 • 80% Black</div>
<div style="color:rgba(0,0,0,.8); font-size:18px; line-height:24px; font-weight:400;">The quick, brown fox</div>

<div class="typography-category">Display-5-Secondary</div>
<div class="typography-label">Size/Leading: 18/24 • Weight: Regular 400 • 40% Black</div>
<div style="color:rgba(0,0,0,.4); font-size:18px; line-height:24px; font-weight:400;">The quick, brown fox</div>

<div class="typography-category">Display-6</div>
<div class="typography-label">Size/Leading: 16/20 • Weight: Semibold 600 • 80% Black</div>
<div style="color:rgba(0,0,0,.8); font-size:16px; line-height:20px; font-weight:600;">The quick, brown fox</div>

<div class="typography-category">Display-6-Secondary</div>
<div class="typography-label">Size/Leading: 16/20 • Weight: Semibold 600 • 40% Black</div>
<div style="color:rgba(0,0,0,.4); font-size:16px; line-height:20px; font-weight:600;">The quick, brown fox</div>

<div class="typography-category">Body</div>
<div class="typography-label">Size/Leading: 14/20 • Weight: Regular 400 • 80% Black</div>
<div style="color:rgba(0,0,0,.8); font-size:14px; line-height:20px; font-weight:400;">Lorem ipsum dolor sit amet, an usu nobis munere. Tractatos definitiones ius ea, soluta diceret accusamus sed ei. Sint eripuit epicuri ut eam, inani tractatos prodesset sea ea, eum eu graecis lucilius. Sapientem molestiae ex cum, ius an habeo blandit, tamquam feugait no sea. Quo eu inermis deseruisse. Est ex quem viderer.</div>

<div class="typography-category">Body-Secondary</div>
<div class="typography-label">Size/Leading: 14/20 • Weight: Regular 400 • 40% Black</div>
<div style="color:rgba(0,0,0,.4); font-size:14px; line-height:20px; font-weight:400;">Ut accusam placerat nec, convenire inciderint te his. Audiam molestie et sea, usu in inani docendi, wisi dictas percipitur an mel. Assum denique aliquando eos te, vel an putent denique ancillae. Nam cu sumo meis impetus.</div>

<div class="typography-category">Caption</div>
<div class="typography-label">Size/Leading: 12/16 • Weight: Regular 400 • 80% Black</div>
<div style="color:rgba(0,0,0,.8); font-size:12px; line-height:16px; font-weight:400;">Pri ad decore persecuti, ea cibo semper accusata sed. Legimus oportere nec ea, pro causae mollis constituto ei. Sed et cetero dissentiet suscipiantur. Ex est quis aliquam, vero nobis omittam sit te. Nibh falli id cum.</div>

<div class="typography-category">Caption-Secondary</div>
<div class="typography-label">Size/Leading: 12/16 • Weight: Regular 400 • 40% Black</div>
<div style="color:rgba(0,0,0,.4); font-size:12px; line-height:16px; font-weight:400;">Lorem ipsum dolor sit amet, mel sonet congue possit at, vel choro tamquam necessitatibus an. Illud suscipiantur definitionem eum no, putent argumentum cum et. Duo atomorum antiopam id, dicam utamur appellantur ex sit. Clita dictas quaestio id mel. Per eleifend electram ne.</div>

<div class="typography-category">Micro</div>
<div class="typography-label">Size/Leading: 11/14 • Weight: Regular 300 • 40% Black</div>
<div style="color:rgba(0,0,0,.4); font-size:11px; line-height:14px; font-weight:300;">Regione suscipit laboramus vel ne, ne diam reformidans eam. Pro quas suavitate eu, oblique fierent vis in. Sea dicta consequat te, nonumy urbanitas voluptaria has no. Quo dolorum molestiae adversarium ad, zril corpora eos ea, has ut perfecto erroribus. Iusto quidam contentiones vim ne, ius ut idque habemus. Ne meis phaedrum pri.</div>

<div class="typography-category">Label</div>
<div class="typography-label">Size/Leading: 11/14 • Letter Spacing: 1 • Weight: Semibold 600 • 40% Black</div>
<div style="color:rgba(0,0,0,.4); font-size:11px; line-height:14px; letter-spacing:1px; font-weight:600;">Eu repudiare similique vix. Lorem ceteros ad vix. Libris tritani deserunt quo id, case audire sed eu. Ad adhuc assentior usu, has unum partem moderatius ex, eu sea alia salutandi ullamcorper. In quot reque voluptatibus quo, everti aperiam civibus no his.</div>

<div class="typography-category">Label-Field</div>
<div class="typography-label">Size/Leading: 12/14 • Weight: Semibold 600 • 40% Black</div>
<div style="color:rgba(0,0,0,.4); font-size:12px; line-height:14px; font-weight:600;">Mea causae impetus ne. Minim fabulas saperet ea pro, eripuit invidunt cum ex. An dicunt platonem duo. Vis at sonet quaeque, fastidii conceptam sea cu, pro choro impetus ea. Et mei tota graece nemore.</div>
