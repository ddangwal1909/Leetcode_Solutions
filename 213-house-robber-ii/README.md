<h2><a href="https://leetcode.com/problems/house-robber-ii/">213. House Robber II</a></h2><h3>Medium</h3><hr><div><p>You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are <strong>arranged in a circle.</strong> That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and&nbsp;<b>it will automatically contact the police if two adjacent houses were broken into on the same night</b>.</p>

<p>Given an integer array <code>nums</code> representing the amount of money of each house, return <em>the maximum amount of money you can rob tonight <strong>without alerting the police</strong></em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<div class="snipit-button extension-button" data-sig="3769f8d899284e5e39c7e0843c9fb68a" style="border-bottom: 0px; border-radius: 3px 3px 0px 0px; padding-bottom: 2px;">{ Snip }</div><pre style="margin-top: 0px;"><strong>Input:</strong> nums = [2,3,2]
<strong>Output:</strong> 3
<strong>Explanation:</strong> You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
</pre>

<p><strong>Example 2:</strong></p>

<div class="snipit-button extension-button" data-sig="dbaa5c2967c729d711ab8a95cc4b4d21" style="border-bottom: 0px; border-radius: 3px 3px 0px 0px; padding-bottom: 2px;">{ Snip }</div><pre style="margin-top: 0px;"><strong>Input:</strong> nums = [1,2,3,1]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
</pre>

<p><strong>Example 3:</strong></p>

<div class="snipit-button extension-button" data-sig="65439ff768aafc293536deabb7e4f485" style="border-bottom: 0px; border-radius: 3px 3px 0px 0px; padding-bottom: 2px;">{ Snip }</div><pre style="margin-top: 0px;"><strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<div class="snipit-button extension-button" data-sig="94fe88c438626183c73895e55e84df5f" style="border-bottom: 0px; border-radius: 3px 3px 0px 0px; padding-bottom: 2px;">{ Snip }</div><ul style="margin-top: 0px;">
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
</ul>
</div>