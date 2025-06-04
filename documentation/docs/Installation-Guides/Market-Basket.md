---
stoplight-id: v2jbhjk3yl9my
---

<div class="col-md-12 content-panel">
                <h2>Market Basket</h2>
                <p></p><p>Thanks for installing and test-driving <span id="title">Call Center (Inbound) Staff Performance</span>! This guide is intended to help you connect this app to your own data. The first step is to ensure that your data follows the same schema (or structure) of the sample datasets that are currently powering the app. Fortunately, Domo has created some powerful data transformation tools to help, along with the step-by-step instructions provided below.</p>
<div id="Step%201:%20Identify%20Required%20Data%20Fields" class="doc-row">
<h3 class="doc-row-title">Step 1: Prepare Your Data</h3>
<div class="small-pad-bottom">
<p>This app requires creating the following custom datasets. To do this, you’ll need to ensure that you have each of these fields in Domo. Then you’ll need to use transforms to create datasets that follow the exact structure or schema of the datasets below. For help with Dataflows, Magic ETL, or BeastModes, please visit <a href="https://university.domo.com/" target="_blank">Domo University</a>.</p>
<h4><strong><span class="s1">Requirements</span></strong></h4>
<ul class="ul1">
<li class="li2"><span class="s1">The dataset that powers this app is the output of an analysis that we conduct using the R language. To run the R script, you will need a computer with R installed and some basic programming experience.&nbsp;</span></li>
<li class="li2"><span class="s1">Required R libraries</span>
<ul class="ul2">
<li class="li2"><span class="s1">arules. We use the apriori algorithm function from the arules library to do the analysis.&nbsp;</span></li>
<li class="li2"><span class="s1">stringr</span></li>
</ul>
</li>
<li><span class="s1">Limitations: depending on the machine on which you are running the analysis, you may run into data-size issues.&nbsp;</span></li>
<li class="li2"><span class="s1">Time frame: you can limit the size of your data by including transactions for a shorter time period.&nbsp;</span></li>
<li class="li2"><span class="s1">Thresholds: you may receive a lot of rules when running the analysis. You can limit the number of rules returned by increasing the support and confidence minimums.</span></li>
</ul>
<h4><strong><span class="s1">Input Requirements</span></strong></h4>
<ul class="ul1">
<li class="li2"><span class="s1">The R script requires a dataset with two columns: Transaction ID and SKU.</span></li>
<li class="li2"><span class="s1">In the provided R script, you can map your column and files names to the provided variables for&nbsp;transactions and SKUs. e.g. If your dataset has a column labeled ‘product ID’ you can map this value to ’SKUs’ in the R-script.&nbsp;</span></li>
</ul>
<h4><strong><span class="s1">Output Interpretation</span></strong></h4>
<ul class="ul3">
<li class="li2"><span class="s1">Support: the percentage of your transactions that have both sides (X and Y) of the rule in them.&nbsp;</span></li>
<li class="li2"><span class="s1">Confidence: the percentage likelihood that Y is in the transaction, given that X is in the transaction.</span></li>
<li class="li2"><span class="s1">Lift: a ratio that indicates how many times more likely a customer is to purchase a product (Y), given that they’re purchasing something else. In other words, if a customer has X in their cart, it is the likelihood that a customer purchases Y, divided by the unconditioned likelihood that they buy Y.&nbsp;</span>
<ul class="ul3">
<li class="li2"><span class="s1">For example, if 5% of your transactions have peanut butter, but of 40% of your transactions with jelly in them also have peanut butter, then your lift on jelly to peanut butter is 8.&nbsp;</span></li>
</ul>
</li>
</ul>
<ul class="ul1">
<ul class="ul2">
<li class="li2"><span class="s1">Rules: The algorithm produces a series of “rules” that indicate relationships between your products. The rules consist of a predictor (X) predicted (Y) relationship.&nbsp;X can consist of a single SKU or multiple SKUs that predict how likely a single SKU (Y) is to occur.</span></li>
<li class="li2"><span class="s1">Parameter interpretation</span></li>
</ul>
</ul>
<h4><strong><span class="s1">Alternative Method with Self Join</span></strong></h4>
<ul class="ul1">
<li class="li2"><span class="s1">If running the R script is beyond your resources, a less-insightful, but helpful, approach is to find frequent pairs using Dataflows to self-join your transactional data. Information on this approach may be found elsewhere.&nbsp;</span></li>
</ul>
<h4><strong><span class="s1">Script:&nbsp;</span></strong></h4>
<p class="p3"><span class="s1">##Load packages</span></p>
<p class="p3"><span class="s1">library(“arules”)</span></p>
<p class="p3"><span class="s1">library(“stringr”)</span></p>
<p class="p3"><span class="s1">##SET PARAMETERS</span></p>
<p class="p3"><span class="s1">trans &lt;- ” ##transaction column name</span></p>
<p class="p3"><span class="s1">sku &lt;- ” ##SKU column name</span></p>
<p class="p3"><span class="s1">dir &lt;- ” ##directory to your file</span></p>
<p class="p3"><span class="s1">setwd(dir)</span></p>
<p class="p3"><span class="s1">file &lt;- ‘.csv’ ##input file name</span></p>
<p class="p3"><span class="s1">supThreshold &lt;- 0.01</span></p>
<p class="p3"><span class="s1">confThreshold &lt;- 0.005</span></p>
<p class="p3"><span class="s1">##Create transaction + sku dataset</span></p>
<p class="p3"><span class="s1">data &lt;- read.csv(file)[,c(trans,sku)]</span></p>
<p class="p3"><span class="s1">data &lt;- unique(data)&nbsp;</span></p>
<p class="p3"><span class="s1">data &lt;- subset(data, get(sku) !=’\N’)</span></p>
<p class="p3"><span class="s1">colnames(data) &lt;- c(‘trans’,’sku’)</span></p>
<p class="p3"><span class="s1">##Get item list and number it.&nbsp;</span></p>
<p class="p3"><span class="s1">itemList &lt;- unique(data.frame(data$sku))&nbsp;</span></p>
<p class="p3"><span class="s1">itemList &lt;- data.frame(itemList,c(1:nrow(itemList)))</span></p>
<p class="p3"><span class="s1">colnames(itemList) &lt;- c(‘sku’,’id’)</span></p>
<p class="p3"><span class="s1">##Merge with transaction + sku dataset.&nbsp;</span></p>
<p class="p3"><span class="s1">##Now we have a unique identifier for each sku, rather than the sku name.&nbsp;</span></p>
<p class="p3"><span class="s1">##We found issues that long SKU names would be truncated to integers when casting as a transaction data type.&nbsp;</span></p>
<p class="p3"><span class="s1">##We deliberately do this here, then bring the names back in later.&nbsp;</span></p>
<p class="p3"><span class="s1">dataset &lt;- merge(data,itemList, all.x = TRUE)</span></p>
<p class="p3"><span class="s1">##split and cast as transaction type</span></p>
<p class="p3"><span class="s1">i &lt;- with(dataset, split(id,trans))</span></p>
<p class="p3"><span class="s1">txn &lt;- as(i, “transactions”)</span></p>
<p class="p3"><span class="s1">itemInfo(txn) &lt;- data.frame(labels = itemList$sku)</span></p>
<p class="p3"><span class="s1">##Create basket rules</span></p>
<p class="p3"><span class="s1">basket_rules &lt;- apriori(txn, parameter = list(sup = supThreshold, conf = confThreshold, target=”rules”))</span></p>
<p class="p3"><span class="s1">##Create output datasets</span></p>
<p class="p3"><span class="s1">q &lt;- data.frame(x = labels(lhs(basket_rules)), y = labels(rhs(basket_rules)), basket_rules@quality)</span></p>
<p class="p3"><span class="s1">q$x &lt;- str_replace_all(q$x, ‘[{}]’, ”)</span></p>
<p class="p3"><span class="s1">q$y &lt;- str_replace_all(q$y, ‘[{}]’, ”)</span></p>
<p class="p3"><span class="s1">q &lt;- q[q$x!=”,]</span></p>
<p class="p3"><span class="s1">outputRules &lt;- q[order(q$lift, decreasing = TRUE),]</span></p>
<p class="p3"><span class="s1">write.csv(outputRules, file = “market_basket_rules.csv”)</span></p>
<p class="p3"><span class="s1">ys &lt;- sort(unique(outputRules$y))</span></p>
<p class="p3"><span class="s1">outputList &lt;- rbind(data.frame(y = ”, label = ‘All’), data.frame(y = ys, label = ys))</span></p>
<p class="p3"><span class="s1">write.csv(outputList, file = “market_basket_list.csv”)</span></p>
</div>
<br>
<div class="doc-row medium-pad-top">
                <h3 class="doc-row-title">Step 2: Connect Your Data</h3>
                <div class="small-pad-bottom">
                    <p>Once you've finished preparing your data as outlined in Step 1 you're ready to connect it to your app. To do this, go to the page in Domo where the app is installed and click the "CONNECT YOUR DATA" button at the top of the page.</p>
                    <p class="small-pad">
                    <img class="alignnone size-full wp-image-1207" src="https://s3.amazonaws.com/development.domo.com/wp-content/uploads/2016/03/14155707/Screen-Shot-2016-03-14-at-3.52.48-PM1.png" alt="Screen Shot 2016-03-14 at 3.52.48 PM" width="1158" height="71">
                    </p>
                    <div id="ooyalaplayer-IyYTc1MjE61NwLdtrxXvZuhH-dSGbWnR" class="ooyalaplayer"></div>
                    <script>
                        OO.ready(function() {
                            OO.Player.create("ooyalaplayer-IyYTc1MjE61NwLdtrxXvZuhH-dSGbWnR", "IyYTc1MjE61NwLdtrxXvZuhH-dSGbWnR", {
                                height: 380
                            });
                        });
                    </script>
                </div>
                <h3 class="doc-row-title">Additional help</h3>
                <div class="small-pad-bottom">
                    <p>Need additional assistance? Visit the <a href="https://dojo.domo.com">Domo Community</a></p>
                </div>
            </div></div>
<p></p>            </div>
