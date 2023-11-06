package lab4_4;
import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

public class lab4_4 extends JFrame {
    private JPanel canvas;
    private JButton inflateButton;
    private Timer timer;
    private int diameter;
    private final int MAX_HEIGHT = 300;
    private final int INFLATION_RATE = 10;

    public lab4_4() {
        setTitle("Balloon Inflation");
        setSize(400, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        canvas = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                g.setColor(Color.RED);
                g.fillOval(getWidth()/2 - diameter/2, getHeight() - diameter - 50, diameter, diameter);
            }
        };
        add(canvas, BorderLayout.CENTER);

        inflateButton = new JButton("Inflate");
        inflateButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (diameter + INFLATION_RATE <= MAX_HEIGHT) {
                    diameter += INFLATION_RATE;
                    canvas.repaint();
                }
                else {
                	ImageIcon img = new ImageIcon(new ImageIcon("rozetka.png").getImage().getScaledInstance(400, 400, Image.SCALE_SMOOTH)); 
                	JLabel picLabel = new JLabel(img);
                	canvas.updateUI();
                	//canvas.imageUpdate(getIconImage(), ALLBITS, MAXIMIZED_BOTH, MAXIMIZED_BOTH, MAXIMIZED_BOTH, MAXIMIZED_BOTH)
                	canvas.add(picLabel);
                	
                	
                	
                	}
            }
        });
        add(inflateButton, BorderLayout.SOUTH);

        setVisible(true);
    }

    public static void main(String[] args) {
        new lab4_4();
    }
}