# 🐕 Visualization Showcase - Crufts Dog Show Analytics

A comprehensive data visualization project showcasing interactive charts and graphs built with D3.js v7, analyzing Crufts Dog Show participation data and historical trends.

## 🌟 Features

### 📊 Interactive Visualizations
- **Visualization 1**: Dog Show Participation Statistics
  - Interactive pie chart showing day-wise attendance distribution
  - Dynamic bar chart displaying top 5 breeds by day
  - Hover interactions and smooth transitions
  
- **Visualization 2**: Breed Performance Analysis
  - **Sunburst Chart**: Hierarchical view of dog groups and breed points
  - **Bar Chart**: Group performance comparison over 20 years
  - Toggle between two different visualization types
  
- **Visualization 3**: Historical Timeline & Geographic Analysis
  - Interactive timeline of Crufts milestones
  - Geographic visualization with London venue locations
  - Animated line charts showing participation trends
  - World War period highlighting

### 🎨 Modern UI/UX
- **Dark/Light Theme Toggle**: Full theme switching with localStorage persistence
- **Responsive Design**: Mobile-friendly layout with touch interactions
- **Loading States**: Smooth loading animations and error handling
- **Accessibility Features**: ARIA labels, keyboard navigation (1, 2, 3 keys)
- **Smooth Animations**: GSAP-powered transitions and D3.js animations

### 🔧 Technical Excellence
- **D3.js v7**: Latest version with modern ES6+ features
- **Dynamic Data Loading**: CSV-based data management
- **Error Handling**: Graceful error states and user feedback
- **Performance Optimized**: Efficient DOM manipulation and data processing
- **Cross-browser Compatible**: Works across all modern browsers

## 🗂️ Project Structure

```
Visualisation_Showcase/
├── README.md
└── dep/
    ├── index.html              # Main application entry point
    ├── vis1.html              # Participation statistics visualization
    ├── vis2a.html             # Sunburst chart visualization
    ├── vis2b.html             # Bar chart visualization
    ├── vis3.html              # Historical timeline visualization
    ├── data.csv               # Main historical data (1886-2024)
    ├── vis1_data.csv          # Breed participation data
    ├── vis2a_data.csv         # Breed points data for sunburst
    └── vis2b_data.csv         # Group performance data
```

## 🚀 Getting Started

### Prerequisites
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Web server (for local development)

### Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd Visualisation_Showcase-main
   ```

2. **Serve Locally**
   ```bash
   # Using Python 3
   python -m http.server 8000
   
   # Using Node.js
   npx http-server
   
   # Using PHP
   php -S localhost:8000
   ```

3. **Open in Browser**
   ```
   http://localhost:8000/dep/
   ```

### Quick Start
1. Open `dep/index.html` in a web browser
2. Use navigation buttons or keyboard shortcuts (1, 2, 3) to explore visualizations
3. Toggle between light/dark themes using the theme button
4. For Visualization 2, use the toggle button to switch between chart types

## 📈 Data Sources

### Primary Dataset (`data.csv`)
- **Time Range**: 1886-2024 (138 years of Crufts history)
- **Columns**: Year, Location, Participants, Description
- **Key Insights**: Venue changes, participant growth, historical milestones

### Visualization-Specific Data
- **`vis1_data.csv`**: Breed participation by day and category
- **`vis2a_data.csv`**: Breed points for sunburst visualization
- **`vis2b_data.csv`**: Group performance statistics

## 🎯 Key Visualizations Explained

### 1. Dog Show Participation Statistics
- **Purpose**: Show daily attendance distribution and top breeds
- **Interactions**: Hover over pie segments to update bar chart
- **Data**: 20 breeds across 4 days, categorized by dog groups

### 2. Breed Performance Analysis
- **Sunburst**: Hierarchical view of groups → breeds → points
- **Bar Chart**: Comparative analysis of Best in Show vs Reserve awards
- **Toggle**: Switch between visualization types seamlessly

### 3. Historical Timeline
- **Timeline**: Major milestones from 1886-2024
- **Geographic**: London venue locations with interactive map
- **Trends**: Participation growth over decades
- **Special Features**: World War period highlighting

## 🛠️ Technical Implementation

### D3.js v7 Features Used
- **Data Loading**: `d3.csv()` for dynamic data import
- **Scales**: Linear, band, ordinal, and point scales
- **Shapes**: Pie, arc, line generators
- **Animations**: Smooth transitions and enter/exit patterns
- **Interactions**: Mouse events, tooltips, hover effects

### Modern JavaScript Features
- **Async/Await**: For data loading and error handling
- **ES6 Modules**: Clean code organization
- **Arrow Functions**: Concise syntax throughout
- **Template Literals**: Dynamic HTML generation

### CSS3 & Styling
- **CSS Variables**: Theme-based color management
- **Flexbox/Grid**: Responsive layout system
- **Animations**: CSS keyframes and transitions
- **Media Queries**: Mobile-responsive design

## 🎨 Customization Guide

### Adding New Visualizations
1. Create new HTML file in `dep/` directory
2. Add corresponding CSV data file
3. Update `index.html` navigation
4. Follow existing pattern for loading states

### Modifying Themes
```css
.light { 
    --bg-color: #f3f4f6; 
    --text-color: #111827; 
    --card-bg: #ffffff;
}
.dark { 
    --bg-color: #1f2937; 
    --text-color: #f9fafb; 
    --card-bg: #374151;
}
```

### Data Format Requirements
```csv
# Example format for vis1_data.csv
breed,entries,attendees,category,day
Border Collie,365,288,Pastoral,1
```

## 🔧 Development

### Code Standards
- **ES6+**: Modern JavaScript syntax
- **D3.js v7**: Latest version for all visualizations
- **Responsive**: Mobile-first design approach
- **Accessible**: WCAG 2.1 compliance

### Performance Optimizations
- **Lazy Loading**: Visualizations load on demand
- **Efficient Rendering**: Minimal DOM manipulations
- **Data Caching**: CSV data cached after first load
- **Smooth Animations**: 60fps animations with requestAnimationFrame

## 🐛 Troubleshooting

### Common Issues
1. **CORS Errors**: Serve files through a web server, not file:// protocol
2. **Data Loading Issues**: Check CSV file paths and formats
3. **Animation Performance**: Reduce data points for smoother animations
4. **Browser Compatibility**: Use modern browsers with ES6+ support

### Browser Support
- ✅ Chrome 88+
- ✅ Firefox 85+
- ✅ Safari 14+
- ✅ Edge 88+

## 📱 Mobile Experience

### Touch Interactions
- **Tap Navigation**: Touch-friendly button sizes
- **Swipe Support**: Gesture-based navigation
- **Responsive Layout**: Optimized for mobile screens
- **Performance**: Smooth animations on mobile devices

## 🔮 Future Enhancements

### Planned Features
- [ ] Data export functionality (PNG/SVG)
- [ ] Advanced filtering and search
- [ ] Real-time data updates
- [ ] Additional chart types (treemap, network)
- [ ] Voice navigation support
- [ ] Progressive Web App (PWA) capabilities

### Potential Improvements
- [ ] Machine learning insights
- [ ] Predictive analytics
- [ ] Social sharing features
- [ ] Multi-language support
- [ ] Advanced accessibility features

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **D3.js Community**: For the incredible visualization library
- **Crufts**: For the inspiration and historical data
- **Tailwind CSS**: For the utility-first CSS framework
- **Leaflet**: For the geographic visualization capabilities

---

**Built with ❤️ using D3.js v7, modern JavaScript, and responsive design principles.**

*For questions or support, please open an issue in the repository.*