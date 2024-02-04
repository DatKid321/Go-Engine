import pyparsing as pp 

# input = "ab"

# A = pp.Literal("a")
# B = pp.Literal("b")

# EQUALS = pp.Forward()
# EQUALS <<= A + EQUALS + B | A + B

# print(EQUALS.parse_string(input))

def Syntax():
    PropIdent = pp.Word(pp.alphas.upper())
    PropValue = pp.Regex(r"\[(.*?)\]").add_parse_action(pp.remove_quotes)

    Property = pp.Group(PropIdent + pp.OneOrMore(PropValue))
    Node = pp.Suppress(";") + pp.ZeroOrMore(Property)
    RootNode = Node
    NodeSequence = pp.ZeroOrMore(Node)

    return NodeSequence

eval = Syntax()

input = '''
;B[qd];W[dd];B[oc];W[pp];B[do];W[dq];B[fp];W[qi];B[cf];W[fd]
;B[bd];W[ch];B[ef];W[ck];B[cc];W[dc];B[hc];W[cd];B[bc];W[df]
;B[dg];W[bf];B[be];W[ce];B[cg];W[bg];B[dh];W[ci];B[db];W[eb]
;B[ca];W[ff];B[ee];W[fe];B[fg];W[gg];B[fh];W[de];B[gh];W[hg]
;B[he];W[id];B[hd];W[hf];B[ie];W[hh];B[hi];W[ii];B[ij];W[hj]
;B[gi];W[ji];B[jj];W[ki];B[hk];W[kj];B[bl];W[bk];B[jg];W[jf]
;B[if];W[ig];B[kg];W[nd];B[od];W[nf];B[mg];W[oe];B[pe];W[pf]
;B[qf];W[pg];B[qg];W[ph];B[me];W[ne];B[pj];W[qj];B[pl];W[nc]
;B[ob];W[ld];B[ke];W[pn];B[ni];W[kd];B[jd];W[lf];B[kf];W[lg]
;B[lh];W[kh];B[li];W[kl];B[nm];W[oj];B[oi];W[pk];B[pi];W[qk]
;B[ok];W[mk];B[nj];W[qh];B[pm];W[on];B[lm];W[ml];B[om];W[rm]
;B[qn];W[qo];B[nn];W[jn];B[rl];W[ql];B[qm];W[rn];B[op];W[pq]
;B[oq];W[fq];B[gq];W[gp];B[eq];W[fr];B[fo];W[er];B[hp];W[jp]
;B[jl];W[jk];B[ik];W[kk];B[im];W[ln];B[ko];W[kn];B[mm];W[km]
;B[fc];W[gc];B[gb];W[mp];B[oo];W[po];B[mo];W[lo];B[pr];W[mr]
;B[qq];W[rp];B[nr];W[rr];B[qr];W[rq];B[mf];W[le];B[ng];W[nb]
;B[md];W[mc];B[oa];W[kb];B[fb];W[ed];B[eg];W[fk];B[fj];W[ek]
;B[gf];W[ge];B[ec];W[ih];B[io];W[gk];B[gj];W[gr];B[hq];W[gm]
;B[hn];W[ir];B[cq];W[cr];B[cp];W[ep];B[eo];W[bn];B[cm];W[cn]
;B[dm];W[dn];B[em];W[bm];B[fm];W[hl];B[il];W[cl];B[af];W[bh]
;B[ej];W[gn];B[go];W[re];B[qe];W[rg];B[rf];W[rh];B[hr];W[hs]
;B[mq];W[lq];B[np];W[nq];B[qp];W[ro];B[mq];W[cb];B[bb];W[nq]
;B[og];W[jc];B[ic];W[mq];B[jb];W[kc];B[lb];W[la];B[ma];W[of]
;B[ka];W[lc];B[ns];W[qs];B[nk];W[sf];B[rd];W[ib];B[na];W[dp]
;B[co];W[ja];B[jo];W[kp];B[iq];W[jq];B[ms];W[ls];B[kr];W[lr]
;B[jr];W[is];B[dj];W[dk];B[br];W[bs];B[ar];W[bo];B[bp];W[la]
;B[gs];W[fs];B[ka];W[ps];B[or];W[la];B[gd];W[gf];B[ka];W[ap]
;B[se];W[la];B[ds];W[cs];B[ka];W[lj];B[mj];W[ll];B[ao];W[la]
;B[mb];W[an];B[sg];W[hb]
'''
print(eval.parse_string(input))


