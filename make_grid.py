import sys

# Make an SVG image of a blank, indexed grid.
# Christian Hill, August 2018.

# SIZE is the grid image size, including padding around all sides of PAD.
SIZE = 600
PAD = 40

try:
    n = int(sys.argv[1])
except (IndexError, ValueError):
    print('Usage: {} n\nwhere n is the grid size.'.format(sys.argv[0]))
    sys.exit(1)

# output SVG image filename, size of the grid within the image.
filename = 'blank_grid-{n}x{n}.svg'.format(n=n)
c_size = (SIZE - 2*PAD) / n

def _get_letter_coord(i):
    """Return the letter A, B, C, ... corresponding to i = 1, 2, 3, ..."""
    return chr(i+64)

with open(filename, 'w') as fo:
    # The SVG preamble and styles.
    print('<?xml version="1.0" encoding="utf-8"?>\n'

    '<svg xmlns="http://www.w3.org/2000/svg"\n' + ' '*5 +
         'xmlns:xlink="http://www.w3.org/1999/xlink" width="{}" height="{}" >'
            .format(SIZE, SIZE), file=fo)
    print("""
    <defs>
    <style type="text/css"><![CDATA[

    line {
        stroke-width: 1px;
        stroke: #888;
    }

    ]]></style>
    </defs>
    """, file=fo)

    # We need n+1 lines to mark out n cells and two nested loops; write both
    # coordinate labels in the outer loop.
    v = PAD // 2
    for i in range(n+1):
        if i:
            u = PAD + c_size*(i-0.5)
            print('<text x="{}" y="{}" text-anchor="middle" '
                  'dominant-baseline="central">{}</text>'.format(u, SIZE-v,
                  _get_letter_coord(i)), file=fo)
            print('<text x="{}" y="{}" text-anchor="middle" '
                  'dominant-baseline="central">{}</text>'.format(v, SIZE-u,
                  str(i)), file=fo)
        for j in range(n+1):
            x1 = x2 = PAD + i*c_size
            y1, y2 = PAD, SIZE-PAD
            print('<line x1="{}" y1="{}" x2="{}" y2="{}"/>'.format(
                  x1, y1, x2, y2), file=fo)
            print('<line x1="{}" y1="{}" x2="{}" y2="{}"/>'.format(
                  y1, x1, y2, x2), file=fo)
    print('</svg>', file=fo)
