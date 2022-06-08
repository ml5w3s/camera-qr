from kivy.app import App
from kivy.lang import Builder
from pyzbar.pyzbar import decode

class QrCodeApp(App):

    def build(self):
        return Builder.load_string(
        """
        #:import ZBarCam kivy_garden.zbarcam.ZBarCam
        BoxLayout:
            orientation: 'vertical'
            ZBarCam:
                id: qrcodecam
            Label:
                size_hint: None, None
                size: self.texture_size[8], 50
                text: ' '.join([str(symbol.data) for symbol in qrcodecam.symbols])
        """

        )

if __name__ == '__main__':
    QrCodeApp().run()