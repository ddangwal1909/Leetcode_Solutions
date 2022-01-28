<h2><a href="https://leetcode.com/problems/first-bad-version/">278. First Bad Version</a></h2><h3>Easy</h3><hr><div><p>You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.</p>

<p>Suppose you have <code>n</code> versions <code>[1, 2, ..., n]</code> and you want to find out the first bad one, which causes all the following ones to be bad.</p>

<p>You are given an API <code>bool isBadVersion(version)</code> which returns whether <code>version</code> is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<div class="snipit-button extension-button" data-sig="c22696c299952f76ba9a2b0e0719be7d" style="border-bottom: 0px; border-radius: 3px 3px 0px 0px; padding-bottom: 2px;">{ Snip }</div><pre style="margin-top: 0px;"><strong>Input:</strong> n = 5, bad = 4
<strong>Output:</strong> 4
<strong>Explanation:</strong>
call isBadVersion(3) -&gt; false
call isBadVersion(5)&nbsp;-&gt; true
call isBadVersion(4)&nbsp;-&gt; true
Then 4 is the first bad version.
</pre>

<p><strong>Example 2:</strong></p>

<div class="snipit-button extension-button" data-sig="c37d2055b089b942eb4de79a9c866b1f" style="border-bottom: 0px; border-radius: 3px 3px 0px 0px; padding-bottom: 2px;">{ Snip }</div><pre style="margin-top: 0px;"><strong>Input:</strong> n = 1, bad = 1
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<div class="snipit-button extension-button" data-sig="dfd0d7ce1e0740b5d7cbfba2e1a5bef2" style="border-bottom: 0px; border-radius: 3px 3px 0px 0px; padding-bottom: 2px;">{ Snip }</div><ul style="margin-top: 0px;">
	<li><code>1 &lt;= bad &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>
</div>