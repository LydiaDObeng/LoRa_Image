# Contributing to LoRa Image Transmission System

Thank you for your interest in contributing to this project! This document provides guidelines and instructions for contributing.

## 🎯 Ways to Contribute

- 🐛 Report bugs and issues
- 💡 Suggest new features or enhancements
- 📝 Improve documentation
- 🔧 Submit bug fixes
- ✨ Add new features
- 🧪 Add tests
- 🎨 Improve code quality

## 📋 Before You Start

1. **Check existing issues** to see if your bug/feature has already been reported
2. **Search pull requests** to avoid duplicating efforts
3. **Open an issue** to discuss major changes before investing significant time

## 🔧 Development Setup

### Prerequisites

- Raspberry Pi (3B+ or newer recommended)
- LoRa SX127x modules (minimum 2)
- Python 3.6+
- Git

### Local Setup

1. **Fork the repository** on GitHub

2. **Clone your fork**:
   ```bash
   git clone https://github.com/YOUR-USERNAME/LoRa_Image.git
   cd LoRa_Image
   ```

3. **Add upstream remote**:
   ```bash
   git remote add upstream https://github.com/LydiaDObeng/LoRa_Image.git
   ```

4. **Install dependencies**:
   ```bash
   pip3 install RPi.GPIO spidev Pillow
   ```

5. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 📝 Code Style Guidelines

### Python Style

Follow PEP 8 guidelines:

- Use 4 spaces for indentation (not tabs)
- Maximum line length: 100 characters
- Use descriptive variable names
- Add docstrings to functions and classes

**Example**:
```python
def calculate_snr(rssi, noise_floor=-122.9):
    """
    Calculate Signal-to-Noise Ratio.
    
    Args:
        rssi (float): Received Signal Strength Indicator in dBm
        noise_floor (float): Noise floor in dBm (default: -122.9)
    
    Returns:
        float: Signal-to-Noise Ratio in dB
    """
    return rssi - noise_floor
```

### Comments

- Use comments to explain **why**, not **what**
- Keep comments up-to-date with code changes
- Use inline comments sparingly

### Naming Conventions

- **Functions**: `snake_case` (e.g., `calculate_snr`)
- **Classes**: `PascalCase` (e.g., `LoRaImageTransmitter`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `CHUNK_SIZE`)
- **Variables**: `snake_case` (e.g., `rssi_values`)

## 🧪 Testing

### Before Submitting

1. **Test your changes** on actual hardware
2. **Verify existing functionality** still works
3. **Test edge cases** (large images, weak signals, etc.)
4. **Document any new dependencies**

### Test Checklist

- [ ] Code runs without errors
- [ ] No new warnings generated
- [ ] Existing features still work
- [ ] New features work as expected
- [ ] Documentation updated
- [ ] Comments added where necessary

## 📤 Submitting Changes

### Commit Messages

Write clear, descriptive commit messages:

**Good**:
```
Add adaptive transmission rate based on RSSI

- Monitor RSSI values during transmission
- Adjust delay between packets dynamically
- Improve reliability in varying signal conditions
```

**Bad**:
```
Update code
```

### Pull Request Process

1. **Update your branch** with latest upstream changes:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Push your branch** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

3. **Open a Pull Request** on GitHub:
   - Use a clear title describing the change
   - Reference any related issues (e.g., "Fixes #42")
   - Describe what changed and why
   - Include testing details

4. **Respond to feedback**:
   - Address reviewer comments
   - Make requested changes
   - Push updates to the same branch

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Testing
Describe how you tested your changes

## Related Issues
Fixes #(issue number)

## Screenshots (if applicable)
Add screenshots to help explain your changes
```

## 🐛 Reporting Bugs

### Bug Report Template

When reporting bugs, include:

1. **Description**: Clear description of the bug
2. **Steps to Reproduce**: Numbered steps to reproduce
3. **Expected Behavior**: What should happen
4. **Actual Behavior**: What actually happens
5. **Environment**:
   - Raspberry Pi model
   - OS version
   - Python version
   - LoRa module type
6. **Error Messages**: Complete error output
7. **Screenshots**: If applicable

**Example**:
```markdown
### Bug Description
Image transmission fails after first chunk

### Steps to Reproduce
1. Run Image_Transmitter.py
2. Wait for first chunk to transmit
3. Observe error on second chunk

### Expected Behavior
All chunks should transmit successfully

### Actual Behavior
Program crashes after first chunk with error:
[paste error message]

### Environment
- Raspberry Pi 4B
- Raspberry Pi OS Bullseye
- Python 3.9.2
- HopeRF RFM95W module
```

## 💡 Suggesting Features

### Feature Request Template

When suggesting features:

1. **Problem**: Describe the problem you're trying to solve
2. **Proposed Solution**: Your idea for solving it
3. **Alternatives**: Other solutions you've considered
4. **Additional Context**: Screenshots, diagrams, etc.

## 📚 Documentation

### Documentation Standards

- Use clear, concise language
- Include code examples
- Add screenshots for visual features
- Update README.md if needed
- Keep documentation in sync with code

### Documentation Locations

- **README.md**: Main project documentation
- **Code comments**: Function/class documentation
- **Wiki**: Detailed guides and tutorials (future)
- **Examples**: Sample code in comments

## 🎯 Priority Areas

We're especially interested in contributions for:

1. **Error Correction**: Implementing forward error correction codes
2. **Multi-Format Support**: PNG, BMP, RAW image support
3. **GUI Interface**: User-friendly interface for configuration
4. **Encryption**: Secure image transmission
5. **Video Support**: Extending to video transmission
6. **Testing Framework**: Automated testing infrastructure
7. **Performance Optimization**: Faster transmission, better compression

## ❓ Questions?

- Open an issue with the "question" label
- Check existing documentation
- Review closed issues and PRs

## 📜 Code of Conduct

### Our Standards

- Be respectful and inclusive
- Accept constructive criticism
- Focus on what's best for the project
- Show empathy towards others

### Unacceptable Behavior

- Harassment or discriminatory language
- Trolling or insulting comments
- Public or private harassment
- Publishing others' private information

## 🙏 Recognition

Contributors will be recognized in:
- README.md acknowledgments section
- Release notes
- Project documentation

Thank you for contributing to LoRa Image Transmission System! 🎉
