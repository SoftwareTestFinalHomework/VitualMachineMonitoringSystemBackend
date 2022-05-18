from django.http import JsonResponse
import libvirt


def get_cpu_usage(request):
    # TODO
    conn = libvirt.open("qemu:///system")
    for i in conn.listDomainsID():
        domain = conn.lookupByID(i)
        print(domain.name())
        print(domain.UUIDString())
        print(domain.info())
    conn.close()

    return JsonResponse({
        'cpu_usage': ''
    })
