#Internet Inspection - 30
On his computer, your father left open a browser with the Thyrin Lab Website. Can you find the hidden access code?

## Solution
1. Using developer tools inspect the website and have a look inside the tbody element of the table with the id `content-table`
2. This will reveal the code
   ```
    <table class="rounded" id="content-table">
				<thead>
					<tr>
						<th>Date</th>
						<th>Author</th>
						<th>Paper</th>
						<th>Access Code</th>
					</tr>
				</thead>
				<tbody>
					<tr id="contents">
					   <td>7/21/2014</td>
					   <td>Dr. Claudio Drake</td><td>Towards developing the next generation of robotic assistants for cardiovascular surgery</td>
					   <td>flag_490ce61bc4170f67939709cb57dbacaa9c39bfae</td>
					 </tr>
				</tbody>
		</table>
	```
3. Giving us the flag `flag_490ce61bc4170f67939709cb57dbacaa9c39bfae`
