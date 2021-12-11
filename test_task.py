
log = 'SAC:0|Sacumen|CAAS|2021.2.0|3|MALICIOUS|High|cat=C2 cs1Label=subcat cs1=DNS_TUNNELING cs2Label=vueUrls cs2=https://aws-dev.sacdev.io/alerts?filter=alertId%3D%3D81650 cs3Label=Tags cs3=USA,Finance cs4Label=Url cs4=https://aws-dev.sacdev.io/settings/tir?rules.sort=4%3A1&filter=state%3D%3D2&selected=9739323 cn1Label=severityScore cn1=900 msg=Malicious activity was reported in CAAS\= A threat intelligence rule has been automatically created in DAAS. dhost=bad.com dst=1.1.1.1'
l1 = log.split('|')
def test_fun():
    d1 = {}
    for ele in l1:
        if '=' in ele:
            l2 = ele.split(' ', 11)

            for ele in l2:
                if ". " not in ele:
                    l3 = ele.split('=')
                    d1[l3[0]] = l3[1]
                else:
                    l3 = ele.split('. ')
                    for i in range(len(l3)):
                        l4 = l3[i].split('=', 1)
                        d1[l4[0]] = l4[1]

                    l4 = l3[i].split()
                    for i in l4:
                        if "=" in i:
                            l5 = i.split('=')
                            d1[l5[0]] = l5[1]

    return d1
    print(d1)
    print(type(d1))
#test_fun()


