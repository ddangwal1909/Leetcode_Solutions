<h2><a href="https://leetcode.com/problems/find-the-team-size/">1303. Find the Team Size</a></h2><h3>Easy</h3><hr><div class="sql-schema-wrapper__3VBi"><a class="sql-schema-link__3cEg">SQL Schema<svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2"><path fill-rule="evenodd" d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"></path></svg></a></div><div><p>Table: <code>Employee</code></p>

<div class="snipit-button extension-button" data-sig="734d11ed248706402790b20f19e1cab7" style="border-bottom: 0px; border-radius: 3px 3px 0px 0px; padding-bottom: 2px;">{ Snip }</div><pre style="margin-top: 0px;">+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| employee_id   | int     |
| team_id       | int     |
+---------------+---------+
employee_id is the primary key for this table.
Each row of this table contains the ID of each employee and their respective team.
</pre>

<p>&nbsp;</p>

<p>Write an SQL query to find the team size of each of the employees.</p>

<p>Return result table in <strong>any order</strong>.</p>

<p>The query result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<div class="snipit-button extension-button" data-sig="11dde35c635e4366f7c1ffe0c13f77f8" style="border-bottom: 0px; border-radius: 3px 3px 0px 0px; padding-bottom: 2px;">{ Snip }</div><pre style="margin-top: 0px;"><strong>Input:</strong> 
Employee Table:
+-------------+------------+
| employee_id | team_id    |
+-------------+------------+
|     1       |     8      |
|     2       |     8      |
|     3       |     8      |
|     4       |     7      |
|     5       |     9      |
|     6       |     9      |
+-------------+------------+
<strong>Output:</strong> 
+-------------+------------+
| employee_id | team_size  |
+-------------+------------+
|     1       |     3      |
|     2       |     3      |
|     3       |     3      |
|     4       |     1      |
|     5       |     2      |
|     6       |     2      |
+-------------+------------+
<strong>Explanation:</strong> 
Employees with Id 1,2,3 are part of a team with team_id = 8.
Employee with Id 4 is part of a team with team_id = 7.
Employees with Id 5,6 are part of a team with team_id = 9.
</pre>
</div>