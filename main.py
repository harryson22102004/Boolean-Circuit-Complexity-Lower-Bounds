# Boolean circuit complexity and lower bound techniques
 
def popcount(x, n_bits=8):
    """Population count (sum of bits) — requires Theta(n) gates."""
    return bin(x & ((1<<n_bits)-1)).count('1')
 
def majority(bits):
    """Majority function."""
    return int(bits.count(1)>len(bits)//2)
 
class Circuit:
    def __init__(self, n_inputs):
        self.gates=[]; self.inputs=list(range(n_inputs)); self.n_in=n_inputs
    def add_gate(self, gtype, inputs):
        g={'type':gtype,'inputs':inputs,'id':self.n_in+len(self.gates)}
        self.gates.append(g); return g['id']
    def depth(self, output_gate):
        memo={}
        def d(gid):
            if gid in memo: return memo[gid]
            if gid<self.n_in: memo[gid]=0; return 0
            g=self.gates[gid-self.n_in]
            memo[gid]=1+max(d(inp) for inp in g['inputs'])
            return memo[gid]
        return d(output_gate)
    def size(self): return len(self.gates)
 
def parity_circuit(n):
    """XOR tree for parity — O(n) size, O(log n) depth."""
    c=Circuit(n); nodes=list(range(n))
    while len(nodes)>1:
        new=[]
        for i in range(0,len(nodes),2):
            if i+1<len(nodes): new.append(c.add_gate('XOR',[nodes[i],nodes[i+1]]))
            else: new.append(nodes[i])
        nodes=new
    return c, nodes[0]
 
for n in [4,8,16]:
    c,out=parity_circuit(n)
    print(f"Parity-{n:2d}: size={c.size():3d}, depth={c.depth(out)}")
 
print(f"\nMajority of [1,0,1,1,0]: {majority([1,0,1,1,0])}")
print("Monotone circuit lower bound for majority: Ω(n^{3/2}) (Andreev 1987)")
