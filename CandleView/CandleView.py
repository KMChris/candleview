from matplotlib import ticker, pyplot as plt

def set_interval(prices_open, prices_high, prices_close, prices_low, prices_volume, interval):
    if interval=='D': minutes = 1440
    elif interval=='T': minutes = 10080
    elif interval=='M': minutes = 43200
    elif interval[-1].lower()=='h': minutes = 60*int(interval.lower().replace('h', ''))
    elif interval[-1]=='m': minutes = int(interval.replace('m', ''))
    else: return
    o, h, c, l, v = [], [], [], [], []
    for j in range(0, int(len(prices_open) / minutes)):
        o.append(prices_open[j * minutes])
        try: c.append(prices_close[j * minutes + minutes - 1])
        except: c.append(prices_close[-1])
        highest, lowest, volume = prices_high[j * minutes], prices_low[j * minutes], 0
        for k in range(minutes):
            try:
                if prices_high[j * minutes + k] > highest: highest = prices_high[j * minutes + k]
                if prices_low[j * minutes + k] < lowest: lowest = prices_low[j * minutes + k]
                volume+=prices_volume[j * minutes + k]
            except: pass
        h.append(highest)
        l.append(lowest)
        v.append(volume)
    return o, h, c, l, v

def plot_candles(o, h, c, l, v=None, scale='linear', points=None): #scale='log' TODO lines=None, triangles=None, rectangles=None
    plt.style.use('dark_background')
    plt.rcParams['axes.linewidth'] = 0.5
    plt.rcParams['figure.facecolor'] = '#131722'
    plt.gca().set_facecolor('#131722')
    highest, lowest, max_volume = h[0], l[0], v[0]
    for k in range(len(o)):
        if h[k]>highest: highest=h[k]
        if l[k]<lowest: lowest=l[k]
        if v is not None:
            if v[k]>max_volume: max_volume=v[k]
    for k in range(len(o)):
        if c[k]>=o[k]:
            plt.gca().add_patch(plt.Rectangle((k+1, o[k]), 0.618, (c[k]-o[k]), color='#2BA59A'))
            plt.gca().add_line(plt.Line2D([k+1.309, k+1.309], [l[k], h[k]], color='#2BA59A', linewidth=1))
            if v is not None:
                plt.axvspan(k+0.809, k+1.809, ymax=(v[k]/max_volume/6.18), facecolor='#2BA59A', alpha=0.5)
        else:
            plt.gca().add_patch(plt.Rectangle((k+1, o[k]), 0.618, (c[k]-o[k]), color='#EF5350'))
            plt.gca().add_line(plt.Line2D([k+1.309, k+1.309], [l[k], h[k]], color='#EF5350', linewidth=1))
            if v is not None:
                plt.axvspan(k+0.809, k+1.809, ymax=(v[k]/max_volume/6.18), facecolor='#EF5350', alpha=0.5)
    if points is not None:
        plt.scatter(*points, color='orange', alpha=1)
    plt.yscale(scale)
    if lowest-0.05*(highest-lowest)<0: plt.gca().set_ylim([0, highest+0.05*(highest-lowest)])
    else: plt.gca().set_ylim([lowest-0.05*(highest-lowest), highest+0.05*(highest-lowest)])
    plt.gca().set_xlim([0, len(o)+2])
    plt.gca().grid(True, color='#38414E', linewidth=0.5)
    plt.gca().set_axisbelow(True)
    plt.subplots_adjust(left=0.1, right=1, top=1, bottom=0.05)
    plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(nbins=15))
    plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(nbins=30))
    plt.show()
