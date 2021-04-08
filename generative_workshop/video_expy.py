import com.hamoid.*

videoExport = VideoExport()

sketchname='floweryboi'

def rec():
  if (frameCount == 1):
    videoExport = new VideoExport(this, "../"+sketchname+".mp4")
    videoExport.setFrameRate(60)
    videoExport.startMovie()

  videoExport.saveFrame()
}
