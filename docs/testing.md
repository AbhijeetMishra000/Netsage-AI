# Testing Plan

| Test | Expected |
|---|---|
| C001 VLAN fault | VLAN diagnosis |
| C006 gateway fault | Gateway mismatch |
| C009 DHCP fault | DHCP relay issue |
| C013 routing fault | Missing route |
| C016 OSPF fault | OSPF advertisement |
| C019 DNS fault | DNS record |
| C021 ACL fault | ACL deny |
| C025 NAT fault | NAT overload |
| C028 wireless fault | Guest VLAN |
| API key absent | Fallback without crash |

## Human Review
Run diagnoses and test Accepted, Edited and Rejected. Verify `reviews.csv` and dashboard counters.

## Safety
Verify every diagnosis contains `human_review_required=true`.
