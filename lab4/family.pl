% ============================================
% ฐานความรู้ครอบครัว (Family Knowledge Base) - Lab 4
% สร้างโดยผู้เรียนสำหรับแบบฝึกหัดการสร้างฐานความรู้ด้วย SWI-Prolog
% ============================================

% === FACTS ===

% --- เพศของบุคคล ---
male(somchai).
male(somsak).
male(somyot).
male(prasit).
male(prayut).

female(somying).
female(somporn).
female(mali).
female(malee).
female(manee).

% --- ความสัมพันธ์พ่อแม่-ลูก ---
% รุ่นที่ 1
parent(somchai, somsak).
parent(somchai, somporn).
parent(somying, somsak).
parent(somying, somporn).
parent(prasit, mali).
parent(malee, mali).

% รุ่นที่ 2
parent(somsak, somyot).
parent(somsak, manee).
parent(mali, somyot).
parent(mali, manee).
parent(somporn, prayut).

% === แบบฝึกหัดที่ 1: เพิ่มสมาชิกใหม่ ===
male(wichai).
female(nida).
female(wanida).
parent(somyot, wichai).
parent(somyot, wanida).
parent(nida, wichai).
parent(nida, wanida).

% === แบบฝึกหัดที่ 4: ฐานความรู้ครอบครัวของตัวเอง (10+ คน, 3 รุ่น) ===

% รุ่นที่ 1 (ปู่ย่า ตายาย) - ครอบครัวอื่น
male(somthong).
female(sompet).
male(prayoon).
female(pranee).

% รุ่นที่ 2 (พ่อแม่)
male(somyong).
female(sompai).
male(somrit).
female(somla).
male(sombat).
female(somprasom).

% ความสัมพันธ์พ่อแม่ รุ่นที่ 1 กับ รุ่นที่ 2
parent(somthong, somyong).
parent(somthong, somrit).
parent(sompet, somyong).
parent(sompet, somrit).

parent(prayoon, sombat).
parent(prayoon, somprasom).
parent(pranee, sombat).
parent(pranee, somprasom).

% รุ่นที่ 3 (ลูก)
male(somkit).
female(somporn2).
male(somkid).
female(somjai).

parent(somyong, somkit).
parent(somyong, somporn2).
parent(somrit, somkid).
parent(somrit, somjai).

% === RULES ===

% --- พ่อ และ แม่ ---
father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).

% --- พี่น้อง ---
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.
brother(X, Y) :- sibling(X, Y), male(X).
sister(X, Y) :- sibling(X, Y), female(X).

% --- ปู่ย่าตายาย ---
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
grandfather(X, Y) :- grandparent(X, Y), male(X).
grandmother(X, Y) :- grandparent(X, Y), female(X).

% --- ลุง ป้า น้า อา ---
uncle(X, Y) :- parent(P, Y), sibling(X, P), male(X).
aunt(X, Y) :- parent(P, Y), sibling(X, P), female(X).

% --- ลูกพี่ลูกน้อง ---
cousin(X, Y) :- parent(PX, X), parent(PY, Y), sibling(PX, PY).

% --- บรรพบุรุษ (Recursive) ---
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(Z, Y), ancestor(X, Z).

% --- ลูกหลาน ---
descendant(X, Y) :- ancestor(Y, X).

% --- สายเลือดเดียวกัน ---
related(X, Y) :- ancestor(Z, X), ancestor(Z, Y), X \= Y.

% === แบบฝึกหัดที่ 2: กฎเพิ่มเติม ===

% หลาน (grandchild)
grandchild(X, Y) :- grandparent(Y, X).

% ลูกชาย และ ลูกสาว
son(X, Y) :- parent(Y, X), male(X).
daughter(X, Y) :- parent(Y, X), female(X).

% ปู่/ตา ฝั่งพ่อ และ ฝั่งแม่
paternal_grandfather(X, Y) :- father(X, F), father(F, Y).
maternal_grandfather(X, Y) :- father(X, M), mother(M, Y).

% === ตัวอย่าง Query (คอมเมนต์เป็นตัวอย่างการใช้งาน) ===
% โหลดไฟล์: ?- [family].
% 
% ตัวอย่างการ Query:
% ?- mother(X, manee).           % หาแม่ของมานี
% ?- descendant(X, somchai).     % หาลูกหลานของสมชาย  
% ?- cousin(prayut, somyot).     % ตรวจสอบลูกพี่ลูกน้อง
% ?- aunt(X, manee).             % หาป้าของมานี
% ?- findall(X, related(X, somyot), R). % หาคนที่ related กับสมยศ
