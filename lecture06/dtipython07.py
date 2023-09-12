#break and continue
for x in range(5):
    if x == 3 :
        break; #break ทำงานเมื่อจบ loop
    print(f"SAU{x}")

print("--------------------------------")

for y in range(5):
    if y == 3 :
        continue; # continue ทำงานเมื่อจบรอบนั้น ไปรอบต่อไปทันที
    print(f'DTI{y}')