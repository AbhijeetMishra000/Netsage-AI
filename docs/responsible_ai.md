# Responsible AI

Every AI diagnosis requires human review.

Required decisions:
- Accepted — diagnosis is correct.
- Edited — diagnosis needs correction.
- Rejected — diagnosis is wrong.

Recommended correction cases for the final demonstration:
1. Native VLAN mismatch misidentified as routing.
2. Missing DHCP relay misidentified as DHCP server failure.
3. Wrong static-route next hop.
4. ACL deny misidentified as routing failure.
5. Missing guest-isolation ACL.

For the final submission, reproduce these corrections through actual reviewer decisions and document the real AI output and reason for correction.
