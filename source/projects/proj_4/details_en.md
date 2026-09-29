### Overview
What makes a neighborhood desirable? By analyzing over 200,000 street-level images with advanced computer vision, this project reveals the hidden visual factors—like tree canopies and cycling activity—that drive housing prices in Rotterdam. The findings offer a new lens for understanding how streetscapes directly impact real estate value.

### The Challenge
Traditional real estate models rely heavily on structural basics: square footage, age, and number of rooms. Yet, anyone hunting for a home knows that the feel of a street matters just as much. These standard valuations often miss the broader environmental context, from the tranquility of nearby parks to the roar of a busy highway. As a result, two identical houses can be priced the same on paper, even if one sits on a vibrant, tree-lined avenue and the other on a grey, concrete artery. This blind spot leads to inaccurate property valuations and overlooks the economic value of well-designed public spaces.

### Objectives
- **Quantify** how visual urban features—such as greenery, pedestrians, cars, and bicycles—extracted from street-level imagery influence residential prices in Rotterdam.
- **Compare** the predictive power of traditional linear valuation models against flexible, machine-learning approaches.
- **Map** the spatial footprint of streetscape elements to understand how their economic impact changes with distance from a property.

### Approach
The research team paired 6,691 property listings in Rotterdam with a massive dataset of over 200,000 Google Street View images. They used semantic segmentation—a computer vision technique that acts like a digital highlighter—to measure the exact amount of greenery visible on a street. Additionally, object detection models counted dynamic elements like people, cars, and bicycles in the neighborhood. By feeding these visual metrics into both standard regression and advanced Random Forest models, the study tested how street-level aesthetics predict property values at different neighborhood scales.

### Key Findings
- **Greenery drives house value:** The Urban Greenery Index showed the strongest positive influence on standalone houses. Just a 10% increase in visible greenery boosts property prices by approximately 9.4%, though this benefit levels off after reaching a 40% threshold.
- **Bicycles signal prime apartments:** For apartment listings, the presence of bicycles had the strongest positive effect. Each additional bicycle spotted nearby increased prices by roughly 10.6%, likely serving as a proxy for high-quality cycling infrastructure and neighborhood vitality.
- **Machine learning beats tradition:** Incorporating these image-derived features significantly improved valuation accuracy, with non-linear Random Forest models consistently outperforming traditional linear formulas.
- **Cars decrease desirability:** Across all property types, higher densities of parked or moving cars consistently drove down property values.

### Impact
These findings give urban planners and policymakers hard evidence that sustainable street design makes economic sense. By proving that investments in greenery and cycling infrastructure—and reductions in car dependency—directly boost neighborhood desirability, this research supports more accurate, equitable property taxation. Ultimately, it demonstrates that greening our streets pays dividends for both residents and the city at large.
