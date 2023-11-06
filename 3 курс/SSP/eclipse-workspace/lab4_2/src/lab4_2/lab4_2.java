package lab4_2;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class lab4_2 extends JFrame implements ActionListener {
    private JButton circleButton, squareButton, triangleButton;
    private ShapePanel shapePanel;

    public lab4_2() {
        setTitle("Изменение формы фигуры");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        // Создание панели для отображения фигуры
        shapePanel = new ShapePanel();
        add(shapePanel, BorderLayout.CENTER);

        // Создание кнопок
        circleButton = new JButton("Круг");
        squareButton = new JButton("Квадрат");
        triangleButton = new JButton("Треугольник");

        // Добавление слушателя событий для кнопок
        circleButton.addActionListener(this);
        squareButton.addActionListener(this);
        triangleButton.addActionListener(this);

        // Создание панели для кнопок
        JPanel buttonPanel = new JPanel();
        buttonPanel.add(circleButton);
        buttonPanel.add(squareButton);
        buttonPanel.add(triangleButton);

        add(buttonPanel, BorderLayout.SOUTH);

        pack();
        setVisible(true);
    }

    // Обработка событий нажатия на кнопки
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == circleButton) {
            shapePanel.setShape("circle");
        } else if (e.getSource() == squareButton) {
            shapePanel.setShape("square");
        } else if (e.getSource() == triangleButton) {
            shapePanel.setShape("triangle");
        }
    }

    // Панель для отображения фигуры
    private class ShapePanel extends JPanel {
        private String shape;

        public ShapePanel() {
            shape = "circle";
            setPreferredSize(new Dimension(200, 200));
            
        }

        public void setShape(String shape) {
            this.shape = shape;
            repaint();
        }

        protected void paintComponent(Graphics g) {
            super.paintComponent(g);
            int width = shapePanel.getWidth()/2,height = shapePanel.getHeight()/2;
            if (shape.equals("circle")) {
                g.setColor(Color.RED);
                g.fillOval(width-50, height-50, 100, 100);
            } else if (shape.equals("square")) {
                g.setColor(Color.GREEN);
                g.fillRect(width-50, height-50, 100, 100);
            } else if (shape.equals("triangle")) {
                int[] xPoints = {width, width-50, width+50};
                int[] yPoints = {height-height/2, height+height/5, height+height/5};
                g.setColor(Color.BLUE);
                g.fillPolygon(xPoints, yPoints, 3);
            }
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                new lab4_2();
            }
        });
    }
}