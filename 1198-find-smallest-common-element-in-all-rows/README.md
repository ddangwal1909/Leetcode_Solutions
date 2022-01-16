<h2><a href="https://leetcode.com/problems/find-smallest-common-element-in-all-rows/">1198. Find Smallest Common Element in All Rows</a></h2><h3>Medium</h3><hr><div><p>Given an <code>m x n</code> matrix <code>mat</code> where every row is sorted in <strong>strictly</strong> <strong>increasing</strong> order, return <em>the <strong>smallest common element</strong> in all rows</em>.</p>

<p>If there is no common element, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<div class="snipit-button extension-button" data-sig="122958d214a52724b79ea300b323162a" style="border-bottom: 0px; border-radius: 3px 3px 0px 0px; padding-bottom: 2px;">{ Snip }</div><pre style="margin-top: 0px;"><strong>Input:</strong> mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
<strong>Output:</strong> 5
</pre>

<p><strong>Example 2:</strong></p>

<div class="snipit-button extension-button" data-sig="31f48fc6ac371d601c9294de0785611a" style="border-bottom: 0px; border-radius: 3px 3px 0px 0px; padding-bottom: 2px;">{ Snip }</div><pre style="margin-top: 0px;"><strong>Input:</strong> mat = [[1,2,3],[2,3,4],[2,3,5]]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<div class="snipit-button extension-button" data-sig="53c4be0c46022d71327488a22b20372e" style="border-bottom: 0px; border-radius: 3px 3px 0px 0px; padding-bottom: 2px;">{ Snip }</div><ul style="margin-top: 0px;">
	<li><code>m == mat.length</code></li>
	<li><code>n == mat[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 500</code></li>
	<li><code>1 &lt;= mat[i][j] &lt;= 10<sup>4</sup></code></li>
	<li><code>mat[i]</code> is sorted in strictly increasing order.</li>
</ul>
</div>