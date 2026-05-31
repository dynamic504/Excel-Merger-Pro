import re
import os

source_file = r'c:\Users\vutha\Desktop\project\Noi file excel pro offline\Excel Merger Pro.hta'
release_file = r'c:\Users\vutha\Desktop\project\Noi file excel pro offline\ExcelMergerPro_Release.hta'

with open(source_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract script content
match = re.search(r'(<script language=\"javascript\">)(.*?)(</script>)', content, re.DOTALL | re.IGNORECASE)
if not match:
    print('Could not find script block')
    exit(1)

js_code = match.group(2)

# Convert JS code to array of integers
int_array = [str(ord(c)) for c in js_code]
int_array_str = ','.join(int_array)

obfuscated_js = f'''
var _0x9a8b = [{int_array_str}];
var _0xc7d6 = [];
for(var _0x1=0; _0x1<_0x9a8b.length; _0x1++) {{
    _0xc7d6.push(String.fromCharCode(_0x9a8b[_0x1]));
}}
var _0xe4f5 = document.createElement('script');
_0xe4f5.text = _0xc7d6.join('');
document.getElementsByTagName('head')[0].appendChild(_0xe4f5);
'''

new_content = content[:match.start(2)] + '\n' + obfuscated_js + '\n' + content[match.end(2):]

with open(release_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Successfully created ' + release_file)
