<h2><a href="https://leetcode.com/problems/combination-sum/">39. Combination Sum</a></h2><h3>Medium</h3><hr><div><p>Given an array of <strong>distinct</strong> integers <code>candidates</code> and a target integer <code>target</code>, return <em>a list of all <strong>unique combinations</strong> of </em><code>candidates</code><em> where the chosen numbers sum to </em><code>target</code><em>.</em> You may return the combinations in <strong>any order</strong>.</p>

<p>The <strong>same</strong> number may be chosen from <code>candidates</code> an <strong>unlimited number of times</strong>. Two combinations are unique if the frequency of at least one of the chosen numbers is different.</p>

<p>It is <strong>guaranteed</strong> that the number of unique combinations that sum up to <code>target</code> is less than <code>150</code> combinations for the given input.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<div class="snipit-button extension-button" data-sig="2c6ff5d0b7956721edc1db0015737597" style="border-bottom: 0px; border-radius: 3px 3px 0px 0px; padding-bottom: 2px;">{ Snip }</div><pre style="margin-top: 0px;"><strong>Input:</strong> candidates = [2,3,6,7], target = 7
<strong>Output:</strong> [[2,2,3],[7]]
<strong>Explanation:</strong>
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
</pre>

<p><strong>Example 2:</strong></p>

<div class="snipit-button extension-button" data-sig="2208c4c44b4e9334a1043f208f5b97b7" style="border-bottom: 0px; border-radius: 3px 3px 0px 0px; padding-bottom: 2px;">{ Snip }</div><pre style="margin-top: 0px;"><strong>Input:</strong> candidates = [2,3,5], target = 8
<strong>Output:</strong> [[2,2,2,2],[2,3,3],[3,5]]
</pre>

<p><strong>Example 3:</strong></p>

<div class="snipit-button extension-button" data-sig="bcf6c57132a91c34d587b2342abb9183" style="border-bottom: 0px; border-radius: 3px 3px 0px 0px; padding-bottom: 2px;">{ Snip }</div><pre style="margin-top: 0px;"><strong>Input:</strong> candidates = [2], target = 1
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<div class="snipit-button extension-button" data-sig="296c8e5e677abd98c100e14559582d7c" style="border-bottom: 0px; border-radius: 3px 3px 0px 0px; padding-bottom: 2px;">{ Snip }</div><ul style="margin-top: 0px;">
	<li><code>1 &lt;= candidates.length &lt;= 30</code></li>
	<li><code>1 &lt;= candidates[i] &lt;= 200</code></li>
	<li>All elements of <code>candidates</code> are <strong>distinct</strong>.</li>
	<li><code>1 &lt;= target &lt;= 500</code></li>
</ul>
</div>