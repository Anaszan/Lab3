# Lab 4: การสร้างฐานความรู้ด้วย SWI-Prolog (Family Relations)

## ไฟล์ในโครงการ

- **[family.pl](family.pl)** – ฐานความรู้ครอบครัวที่สมบูรณ์
  - Facts: เพศของบุคคล, ความสัมพันธ์พ่อแม่-ลูก
  - Rules: พ่อ, แม่, พี่น้อง, ปู่ย่าตายาย, ลุงป้า, ลูกพี่ลูกน้อง, บรรพบุรุษ (Recursive)
  - Exercise 1: เพิ่มสมาชิกใหม่ (wichai, nida, wanida)
  - Exercise 2: กฎเพิ่มเติม (grandchild, son, daughter, paternal/maternal_grandfather)
  - Exercise 4: ฐานความรู้ขยายด้วยครอบครัวที่สอง (10+ คน, 3 รุ่น)

- **[run_queries.pl](run_queries.pl)** – Runner สำหรับรัน Query อัตโนมัติ
- **[query_results.txt](query_results.txt)** – ผลลัพธ์ของ Query ตัวอย่าง

## การติดตั้ง SWI-Prolog

### Windows
```bash
# ดาวน์โหลดจาก https://www.swi-prolog.org/download/stable
# เลือก Windows Installer และติดตั้ง
# ตรวจสอบการติดตั้ง:
swipl --version
```

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install swi-prolog
swipl --version
```

### macOS
```bash
brew install swi-prolog
swipl --version
```

## การใช้งาน

### 1. เปิด SWI-Prolog
```bash
cd c:\LAB2\lab4
swipl
```

### 2. โหลดไฟล์ฐานความรู้
```prolog
?- [family].
% หรือ
?- consult('family.pl').
```

### 3. รัน Query ตัวอย่าง

#### Query แบบ Yes/No (ตรวจสอบความจริง)
```prolog
% ถาม: สมชายเป็นพ่อของสมศักดิ์หรือไม่?
?- father(somchai, somsak).
% ตอบ: true.

% ถาม: มะลิเป็นแม่ของสมยศหรือไม่?
?- mother(mali, somyot).
% ตอบ: true.

% ถาม: สมศักดิ์และสมพรเป็นพี่น้องกันหรือไม่?
?- sibling(somsak, somporn).
% ตอบ: true.
```

#### Query แบบหาค่า (ใช้ตัวแปร)
```prolog
% ถาม: ใครเป็นพ่อของสมศักดิ์?
?- father(X, somsak).
% ตอบ: X = somchai.

% ถาม: สมชายเป็นพ่อของใครบ้าง?
?- father(somchai, X).
% ตอบ: X = somsak ;
%       X = somporn.

% ถาม: ใครเป็นปู่ของสมยศ?
?- grandfather(X, somyot).
% ตอบ: X = somchai ;
%       X = prasit.
```

#### Query ขั้นสูง
```prolog
% หาคำตอบทั้งหมดในครั้งเดียว
?- findall(X, father(somchai, X), Children).
% ตอบ: Children = [somsak, somporn].

% หาคำตอบไม่ซ้ำและจัดเรียง
?- setof(X, ancestor(X, somyot), Ancestors).
% ตอบ: Ancestors = [malee, mali, prasit, somchai, somsak, somying].

% ดูข้อมูลทั้งหมดของ predicate
?- listing(parent).

% ออกจากโปรแกรม
?- halt.
```

## โครงสร้างครอบครัว

### ครอบครัวหลัก
```
                    ┌─────────────────┐
         ┌─────────┤   รุ่นที่ 1     ├─────────┐
         │         └─────────────────┘         │
         │                                     │
    ┌────┴────┐                          ┌────┴────┐
    │ สมชาย   │                          │ ประสิทธิ์│
    └────┬────┘                          └────┬────┘
         │  แต่งงาน                           │  แต่งงาน
    ┌────┴────┐                          ┌────┴────┐
    │ สมหญิง  │                          │  มาลี   │
    └────┬────┘                          └────┬────┘
         │
         ├────────────────┬───────────────────┤
         │                │                   │
    ┌────┴────┐     ┌────┴────┐         ┌────┴────┐
    │ สมศักดิ์ │     │  สมพร   │         │  มะลิ   │
    └────┬────┘     └────┬────┘         └────┬────┘
         │               │                   │
         └───────────────┼───────────────────┘
                   แต่งงาน│
                         │
              ┌──────────┴──────────┐
              │                     │
         ┌────┴────┐          ┌────┴────┐     ┌────────┐
         │ สมยศ    │          │  มานี   │     │ wichai │
         └─────────┘          └─────────┘     └────────┘
```

### ครอบครัวที่สอง (Exercise 4)
```
somthong ─── sompet      prayoon ─── pranee
    │            │            │           │
    └─────┬──────┘            └─────┬─────┘
          │                        │
    ┌─────┴──────┐         ┌──────┴─────┐
somyong ─── sompai    sombat ─── somprasom
    │                    │
    ├───┬────────        └───┬────
    │   │                    │
 somkit  somporn2         somkeit
 
somrit ─── somla
    │
    ├───┬────────
    │   │
 somkid somjai
```

## คำสั่งที่มีประโยชน์

| คำสั่ง | ความหมาย |
|--------|--------|
| `?- [family].` | โหลดไฟล์ family.pl |
| `?- listing(predicate).` | แสดง facts และ rules ของ predicate |
| `?- findall(X, goal, List).` | หาคำตอบทั้งหมดเป็น List |
| `?- setof(X, goal, Set).` | หาคำตอบไม่ซ้ำและจัดเรียง |
| `?- bagof(X, goal, Bag).` | หาคำตอบทั้งหมด (อนุญาตให้ซ้ำ) |
| `?- trace.` | เปิด Debug mode |
| `?- notrace.` | ปิด Debug mode |
| `?- halt.` | ออกจากโปรแกรม |

## โครงสร้างของ Prolog

### Facts (ข้อเท็จจริง)
ข้อความที่เป็นจริงเสมอ
```prolog
male(somchai).
parent(somchai, somsak).
```

### Rules (กฎ)
ข้อความที่เป็นจริงเมื่อเงื่อนไขเป็นจริง
```prolog
father(X, Y) :- parent(X, Y), male(X).
```

### Operators
| Operator | ความหมาย |
|----------|--------|
| `:-` | if (ถ้า) |
| `,` | and (และ) |
| `;` | or (หรือ) |
| `\=` | ไม่เท่ากับ |
| `=` | เท่ากับ (unification) |

## เทคนิคการเขียน Prolog ที่ดี

1. ✓ ใช้ชื่อ Predicate ที่มีความหมาย: `parent`, `father`, `mother` แทน `p`, `f`, `m`
2. ✓ แสดง Comment ที่ชัดเจน: ใช้ `%` สำหรับแต่ละบรรทัด
3. ✓ จำไว้ว่า Recursive rules ต้องมี Base case เสมอ
4. ✓ ทดสอบ Facts ก่อน แล้วค่อยทดสอบ Rules
5. ✓ ใช้ `\=` เพื่อหลีกเลี่ยง X = X

## แบบฝึกหัดเพิ่มเติม

### Exercise 3: Query
ลองทำการ Query ต่อไปนี้:
```prolog
% หาแม่ของมานี
?- mother(X, manee).

% หาลูกหลานของสมชาย
?- descendant(X, somchai).

% ตรวจสอบว่าประยุทธ์และสมยศเป็นลูกพี่ลูกน้องกันหรือไม่
?- cousin(prayut, somyot).

% หาป้าของมานี
?- aunt(X, manee).

% หาคนที่มีความเกี่ยวข้องกัน (related) กับสมยศทั้งหมด
?- findall(X, related(X, somyot), RelatedPeople).
```

## เอกสารอ้างอิง

- [SWI-Prolog Official Documentation](https://www.swi-prolog.org/pldoc/)
- [Learn Prolog Now!](http://www.learnprolognow.org/)
- [Prolog Tutorial - TutorialsPoint](https://www.tutorialspoint.com/prolog/)

---

**หมายเหตุ:** Lab 4 นี้ออกแบบมาเพื่อช่วยให้เข้าใจ Predicate Logic และการนำไปใช้ใน Prolog ผ่านตัวอย่างความสัมพันธ์ในครอบครัว
