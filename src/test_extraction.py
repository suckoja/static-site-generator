import unittest
from extraction import extract_markdown_images, extract_markdown_links, extract_markdown_linked_images

class TestExtractMarkDown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [{"type": "image", "alt": "image", "src": "https://i.imgur.com/zjjcJKZ.png"}],
            matches,
        )

    def test_extract_multiple_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        self.assertListEqual(
            [
                {"type": "image", "alt": "rick roll", "src": "https://i.imgur.com/aKaOqIh.gif"},
                {"type": "image", "alt": "obi wan", "src": "https://i.imgur.com/fJRm4Vk.jpeg"},
            ],
            matches,
        )

    def test_extract_markdown_image_with_title(self):
        matches = extract_markdown_images(
            '![An old rock in the desert!](/assets/images/shiprock.jpg "Shiprock, New Mexico by Beau Rogers")'
        )
        self.assertListEqual(
            [
                {
                    "type": "image",
                    "alt": "An old rock in the desert!",
                    "src": '/assets/images/shiprock.jpg "Shiprock, New Mexico by Beau Rogers"',
                }
            ],
            matches,
        )

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual(
            [
                {"type": "link", "text": "to boot dev", "href": "https://www.boot.dev"},
                {"type": "link", "text": "to youtube", "href": "https://www.youtube.com/@bootdotdev"},
            ],
            matches,
        )

    def test_extract_markdown_images_with_linking_images(self):
        matches = extract_markdown_images(
            '[![An old rock in the desert](/assets/images/shiprock.jpg "Shiprock, New Mexico by Beau Rogers")]'
            '(https://www.flickr.com/photos/beaurogers/31833779864/in/photolist-Qv3rFw)'
        )
        self.assertListEqual(
            [
                {
                    "type": "image",
                    "alt": "An old rock in the desert",
                    "src": '/assets/images/shiprock.jpg "Shiprock, New Mexico by Beau Rogers"',
                }
            ],
            matches,
        )

    def test_extract_markdown_link_with_linking_images(self):
        matches = extract_markdown_linked_images(
            '[![An old rock in the desert](/assets/images/shiprock.jpg "Shiprock, New Mexico by Beau Rogers")]'
            '(https://www.flickr.com/photos/beaurogers/31833779864/in/photolist-Qv3rFw)'
        )
        self.assertListEqual(
            [
                {
                    "type": "linked_image",
                    "image_markdown": '![An old rock in the desert](/assets/images/shiprock.jpg "Shiprock, New Mexico by Beau Rogers")',
                    "href": "https://www.flickr.com/photos/beaurogers/31833779864/in/photolist-Qv3rFw",
                }
            ],
            matches,
        )

if __name__ == "__main__":
    unittest.main()
