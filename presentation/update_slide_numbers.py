import re

file_path = '/Users/youngjinson/Desktop/2025-2학기/ba2/ba2_team_project2/25-12-7/presentation_ko.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replacements with context to ensure unique matching
replacements = [
    (
        r'<!-- Slide 6: Model Selection -->\s*<div class="slide-wrapper" id="slide-5">\s*<section class="slide">\s*<span class="slide-number">06 / 11</span>',
        '<!-- Slide 7: Model Selection -->\n<div class="slide-wrapper" id="slide-5">\n    <section class="slide">\n        <span class="slide-number">07 / 11</span>'
    ),
    (
        r'<!-- Slide 7: Airbnb Official Criteria -->\s*<div class="slide-wrapper" id="slide-6">\s*<section class="slide slide-accent">\s*<span class="slide-number" style="color: rgba\(255,255,255,0.5\);">07 / 11</span>',
        '<!-- Slide 8: Airbnb Official Criteria -->\n<div class="slide-wrapper" id="slide-6">\n    <section class="slide slide-accent">\n        <span class="slide-number" style="color: rgba(255,255,255,0.5);">08 / 11</span>'
    ),
    (
        r'<!-- Slide 8: Model vs Rule Comparison -->\s*<div class="slide-wrapper" id="slide-7">\s*<section class="slide">\s*<span class="slide-number">08 / 11</span>',
        '<!-- Slide 9: Model vs Rule Comparison -->\n<div class="slide-wrapper" id="slide-7">\n    <section class="slide">\n        <span class="slide-number">09 / 11</span>'
    ),
    (
        r'<!-- Slide 9: Disagreement Cases -->\s*<div class="slide-wrapper" id="slide-8">\s*<section class="slide slide-gray">\s*<span class="slide-number">09 / 11</span>',
        '<!-- Slide 10: Disagreement Cases -->\n<div class="slide-wrapper" id="slide-8">\n    <section class="slide slide-gray">\n        <span class="slide-number">10 / 11</span>'
    ),
    (
        r'<!-- Slide 10: Conclusion -->\s*<div class="slide-wrapper" id="slide-9">\s*<section class="slide slide-dark">\s*<span class="slide-number" style="color: var\(--gray-500\);">10 / 11</span>',
        '<!-- Slide 11: Conclusion -->\n<div class="slide-wrapper" id="slide-9">\n    <section class="slide slide-dark">\n        <span class="slide-number" style="color: var(--gray-500);">11 / 11</span>'
    )
]

for pattern, replacement in replacements:
    content = re.sub(pattern, replacement, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Slide numbers updated successfully.")





