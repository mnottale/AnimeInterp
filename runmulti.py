import sys
import os
import tempfile
import shutil
from run import run

def run_multi(imagedir, inter_frames, outputdir):
    if not os.path.exists(outputdir):
        os.mkdir(outputdir)
    images = os.listdir(imagedir)
    images.sort()
    oidx = 1
    with tempfile.TemporaryDirectory() as td:
        for idx in range(len(images)-1):
            i1 = os.path.join(imagedir, images[idx])
            i2 = os.path.join(imagedir, images[idx+1])
            run(i1, i2, inter_frames, td)
            shutil.copy(i1, os.path.join(outputdir, '{:04}.png'.format(oidx)))
            oidx += 1
            for intf in range(inter_frames):
                shutil.copy(os.path.join(td, 'frame-{}.png'.format(intf)), os.path.join(outputdir, '{:04}.png'.format(oidx)))
                oidx +=1
    shutil.copy(os.path.join(imagedir, images[len(images)-1]), os.path.join(outputdir, '{:04}.png'.format(oidx)))


if __name__ == '__main__':
    run_multi(sys.argv[1], int(sys.argv[2]), sys.argv[3])