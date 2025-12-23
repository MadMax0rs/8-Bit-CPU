import win32clipboard as cb
import re

cb.OpenClipboard()

CF_HTML = cb.RegisterClipboardFormat("HTML Format")

if not cb.IsClipboardFormatAvailable(CF_HTML):
	quit()
data = cb.GetClipboardData(CF_HTML)

print("\n\n\n\n\n\n\n\n\n\n\n", type(data))
print("\n\n\n\n\n\n\n\n\n\n\n", data)

html = str(data)[str(data).find("<!--StartFragment-->")+20:str(data).find("<!--EndFragment-->")]
cb.EmptyClipboard()
cb.SetClipboardText(str(html))

print("\n\n\n\n\n\n\n\n\n\n\n", html)

html += '''
<script>
	arr = []
	arr.push()
	table = document.getElementById("table").children.item(0)
	for (i = 0; i < table.children.length; i++) {
		tmpArr0 = []
		for (j = 0; j < table.children.item(i).children.length; j++) {
			tmpArr1 = []
			for (k = 0; k < table.children.item(i).children.item(j).children.length; k++) {
				if (table.children.item(i).children.item(j).children.item(k).innerHTML == "<br>")
					continue

				tmpArr1.push(table.children.item(i).children.item(j).children.item(k).innerHTML)
			}
			if (tmpArr1.length < 1)
				continue

			tmpArr0.push(tmpArr1)
		}
		arr.push(tmpArr0)
	}
	console.log(arr)
</script>'''

with open("D:\\Logisim\\8-bit-CPU\\clipboard.html", "w") as file:
	file.write(html)




# Step 1: Extract each row
rows = re.findall(r'<tr>(.*?)</tr>', html, re.DOTALL)

table = []
for row in rows:
    # Step 2: Extract each <td> (cell) in the row
    cells = re.findall(r'<td[^>]*>(.*?)</td>', row, re.DOTALL)
    row_data = []

    for cell in cells:
        # Step 3: Extract text inside each <div> in the cell
        divs: list[str] = re.findall(r'<div[^>]*>(.*?)</div>', cell)
        
        row_data.append([d for d in divs if d != ['<br>']])
    
    table.append(row_data)






#print("\n\n\n\n\n\n\n\n\n\n\n", table)

# "NOP":
# "MOV_REG_IMM":
# "MOV_REG_REG":
# "MOV_REG_MEM":
# "MOV_MEM_IMM":
# "MOV_MEM_REG":
# "MOV_MEM_MEM":
# "ADD_REG_IMM":
# "ADD_REG_REG":
# "ADD_REG_MEM":
# "ADD_MEM_IMM":
# "ADD_MEM_REG":
# "ADD_MEM_MEM":
# "SUB_REG_IMM":
# "SUB_REG_REG":
# "SUB_REG_MEM":
# "SUB_MEM_IMM":
# "SUB_MEM_REG":
# "SUB_MEM_MEM":
# "MUL_REG_IMM":
# "MUL_REG_REG":
# "MUL_REG_MEM":
# "MUL_MEM_IMM":
# "MUL_MEM_REG":
# "MUL_MEM_MEM":
# "DIV_REG_IMM":
# "DIV_REG_REG":
# "DIV_REG_MEM":
# "DIV_MEM_IMM":
# "DIV_MEM_REG":
# "DIV_MEM_MEM":
# "PUSH_IMM":
# "PUSH_REG":
# "PUSH_MEM":
# "POP_REG":
# "POP_MEM":
# "SHL_REG_IMM":
# "SHL_REG_REG":
# "SHR_REG_IMM":
# "SHR_REG_REG":
# "AND_REG_IMM":
# "AND_REG_REG":
# "AND_REG_MEM":
# "AND_MEM_IMM":
# "AND_MEM_REG":
# "AND_MEM_MEM":
# "OR_REG_IMM":
# "OR_REG_REG":
# "OR_REG_MEM":
# "OR_MEM_IMM":
# "OR_MEM_REG":
# "OR_MEM_MEM":
# "XOR_REG_IMM":
# "XOR_REG_REG":
# "XOR_REG_MEM":
# "XOR_MEM_IMM":
# "XOR_MEM_REG":
# "XOR_MEM_MEM":
# "NOT_REG":
# "NOT_MEM":
# "CMP_REG_IMM":
# "CMP_REG_REG":
# "CMP_REG_MEM":
# "CMP_MEM_IMM":
# "CMP_MEM_REG":
# "CMP_MEM_MEM":
# "XCHG_REG_REG":
# "XCHG_REG_MEM":
# "XCHG_MEM_MEM":
# "JMP_IMM":
# "JMP_REG":
# "JZ_IMM":
# "JZ_REG":
# "JNZ_IMM":
# "JNZ_REG":
# "JS_IMM":
# "JS_REG":
# "JNS_IMM":
# "JNS_REG":
# "JG_IMM":
# "JG_REG":
# "JGE_IMM":
# "JGE_REG":
# "JL_IMM":
# "JL_REG":
# "JLE_IMM":
# "JLE_REG":
# "JA_IMM":
# "JA_REG":
# "JAE_IMM":
# "JAE_REG":
# "JB_IMM":
# "JB_REG":
# "JBE_IMM":
# "JBE_REG":
# "JP_IMM":
# "JP_REG":
# "JNP_IMM":
# "JNP_REG":
# "JO_IMM":
# "JO_REG":
# "JNO_IMM":
# "JNO_REG":


cb.CloseClipboard()