package lab4_3;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class lab4_3 extends JFrame implements ActionListener {
    private JButton leftButton;
    private JButton rightButton;
    private ShapePanel shapePanel;

    public lab4_3() {
        setTitle("Shape Movement App");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(400, 300);
        setLocationRelativeTo(null);

        leftButton = new JButton("Left");
        rightButton = new JButton("Right");
        shapePanel = new ShapePanel();

        leftButton.addActionListener(this);
        rightButton.addActionListener(this);

        JPanel buttonPanel = new JPanel();
        buttonPanel.add(leftButton);
        buttonPanel.add(rightButton);

        add(shapePanel, BorderLayout.CENTER);
        add(buttonPanel, BorderLayout.SOUTH);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == leftButton) {
            shapePanel.moveLeft();
        } else if (e.getSource() == rightButton) {
            shapePanel.moveRight();
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                new lab4_3().setVisible(true);
            }
        });
    }
}

class ShapePanel extends JPanel {
    private int xCoordinate;

    public ShapePanel() {
        xCoordinate = 200;
    }

    public void moveLeft() {
        xCoordinate -= 10;
        repaint();
    }

    public void moveRight() {
        xCoordinate += 10;
        repaint();
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.setColor(Color.RED);
        g.fillRect(xCoordinate, 100, 50, 50);
    }
}